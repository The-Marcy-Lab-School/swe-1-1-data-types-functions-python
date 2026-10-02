from default_args import greet
from return_vs_print import add, divide, multiply, subtract


def printed(capsys):
    return [line for line in capsys.readouterr().out.splitlines() if line.strip()]


def test_return_vs_print_returns(capsys):
    """return_vs_print - each function returns its result"""
    assert add(2, 3) == 5
    assert subtract(10, 4) == 6
    assert multiply(3, 4) == 12
    assert divide(10, 2) == 5
    capsys.readouterr()


def test_return_vs_print_still_prints(capsys):
    """return_vs_print - each function still prints its message"""
    add(2, 3)
    assert printed(capsys) == ["The sum of 2 and 3 is 5"]

    divide(10, 2)
    assert printed(capsys) == ["The quotient of 10 and 2 is 5.0"]


def test_return_vs_print_composes(capsys):
    """return_vs_print - a returned value can be passed to another call"""
    assert add(add(1, 2), 3) == 6
    assert multiply(add(1, 1), 5) == 10
    capsys.readouterr()


def test_greet_only_needs_a_name():
    """greet - works with only a name"""
    assert greet("Alice") == "Hello, Alice!"


def test_greet_accepts_overrides():
    """greet - accepts a different greeting and punctuation"""
    assert greet("Bob", "Hi") == "Hi, Bob!"
    assert greet("Dev", punctuation=".") == "Hello, Dev."
    assert greet(greeting="Yo", name="Eve") == "Yo, Eve!"
    assert greet("Ada", "Welcome", "?") == "Welcome, Ada?"
