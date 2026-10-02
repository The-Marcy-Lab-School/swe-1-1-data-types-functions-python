import inspect

from bad_scope import describe_mood


def printed(capsys):
    return [line for line in capsys.readouterr().out.splitlines() if line.strip()]


def test_describe_mood_output(capsys):
    """describe_mood - prints both sentences in the right order"""
    describe_mood()
    assert printed(capsys) == [
        "Hello Zo, are you feeling happy today?",
        "Oh no, I'm sorry you're feeling sad today.",
    ]


def test_describe_mood_uses_f_strings():
    """describe_mood - uses f-strings and no global"""
    source = inspect.getsource(describe_mood)
    assert "global" not in source
    assert "+" not in source
    assert 'f"' in source or "f'" in source
