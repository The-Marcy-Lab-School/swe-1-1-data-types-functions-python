from from_scratch import (
    calculate_area,
    convert_to_fahrenheit,
    create_greeting,
    is_even,
    is_valid_age,
)


def test_calculate_area():
    """calculate_area - returns width times height"""
    assert calculate_area(5, 3) == 15
    assert calculate_area(10, 7) == 70
    assert calculate_area(1, 1) == 1
    assert calculate_area(0, 9) == 0


def test_is_even():
    """is_even - returns True for even numbers and False for odd ones"""
    assert is_even(2) is True
    assert is_even(0) is True
    assert is_even(-4) is True
    assert is_even(3) is False
    assert is_even(-7) is False


def test_convert_to_fahrenheit():
    """convert_to_fahrenheit - converts celsius to fahrenheit"""
    assert convert_to_fahrenheit(0) == 32
    assert convert_to_fahrenheit(100) == 212
    assert convert_to_fahrenheit(-40) == -40
    assert convert_to_fahrenheit(37) == 98.6


def test_is_valid_age():
    """is_valid_age - returns True for 0 through 120 inclusive"""
    assert is_valid_age(0) is True
    assert is_valid_age(25) is True
    assert is_valid_age(120) is True
    assert is_valid_age(-1) is False
    assert is_valid_age(121) is False


def test_create_greeting():
    """create_greeting - returns a greeting with the name in it"""
    assert create_greeting("Alice") == "Hello, Alice!"
    assert create_greeting("Zo") == "Hello, Zo!"
    assert create_greeting("") == "Hello, !"
