"""Turn pytest's JUnit XML into a score the student and the gradebook can read.

Writes two things from one source:

  1. A table appended to the Actions job summary, which is what the student
     reads after a push.
  2. A commit status under the context "marcy/score", which is what the
     gradebook collector reads back through the API.

Both come from the same XML, so they cannot disagree.
"""

import os
import subprocess
import sys
import xml.etree.ElementTree as ET
from collections import defaultdict

PASS_MARK = 0.75


def suite_of(case):
    """Group by the test file, which is how assignments are already split."""
    path = case.get("file") or case.get("classname", "")
    name = path.rsplit("/", 1)[-1].removesuffix(".py")
    return name.removeprefix("test_").replace("_", " ").title() or "Tests"


def main(xml_path):
    # No XML means pytest could not start: a syntax error, or a missing import.
    # That is a real result and must not be reported as a crash of the grader.
    if not os.path.exists(xml_path):
        write_summary("Tests could not run. Check the log above for the error.")
        set_status("error", "tests could not run")
        return

    root = ET.parse(xml_path).getroot()
    cases = root.iter("testcase")

    suites = defaultdict(lambda: [0, 0])
    for case in cases:
        passed = not any(case.find(t) is not None
                         for t in ("failure", "error", "skipped"))
        s = suites[suite_of(case)]
        s[1] += 1
        s[0] += int(passed)

    total_pass = sum(p for p, _ in suites.values())
    total = sum(t for _, t in suites.values())
    pct = round(100 * total_pass / total) if total else 0
    complete = pct >= PASS_MARK * 100

    lines = ["| Suite | Passed |", "| --- | --- |"]
    for name in sorted(suites):
        p, t = suites[name]
        lines.append(f"| {name} | {p}/{t} |")
    lines.append(f"| **Total** | **{total_pass}/{total} ({pct}%)** |")
    lines.append("")
    lines.append(
        f"{'Complete' if complete else 'Not yet complete'} — "
        f"{int(PASS_MARK * 100)}% of tests passing counts as complete."
    )
    write_summary("\n".join(lines))

    # "pending" rather than "failure" below 75%. A red X on every push until a
    # student is done tells them they have failed, when what is true is that
    # they are not finished. Marcy's stated position is that submitting
    # unfinished work is correct, so the check stays neutral until it is green.
    set_status(
        "success" if complete else "pending",
        f"{total_pass}/{total} ({pct}%) "
        f"{'complete' if complete else 'keep going'}",
    )


def write_summary(markdown):
    path = os.environ.get("GITHUB_STEP_SUMMARY")
    if not path:
        print(markdown)
        return
    with open(path, "a", encoding="utf-8") as f:
        f.write("## Your score\n\n" + markdown + "\n")


def set_status(state, description):
    """Post the commit status the gradebook reads. Never fail the job over it."""
    repo, sha = os.environ.get("REPO"), os.environ.get("SHA")
    if not (repo and sha):
        return
    try:
        subprocess.run(
            ["gh", "api", "-X", "POST", f"repos/{repo}/statuses/{sha}",
             "-f", f"state={state}",
             "-f", "context=marcy/score",
             "-f", f"description={description[:140]}"],
            check=False, capture_output=True,
        )
    except OSError:
        pass


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "results.xml")
