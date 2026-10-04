from from_scratch import (
    calculate_area,
    convert_to_fahrenheit,
    calculate_room_cost,
    create_greeting,
    is_even,
    is_leap_year,
    is_valid_age,
    is_vowel,
    make_banner,
    minutes_to_clock,
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
    """convert_to_fahrenheit - converts celsius to fahrenheit, always returns a float"""
    assert convert_to_fahrenheit(0) == 32
    assert convert_to_fahrenheit(100) == 212
    assert convert_to_fahrenheit(-40) == -40
    assert convert_to_fahrenheit(37) == 98.6
    assert isinstance(convert_to_fahrenheit(0), float)
    assert isinstance(convert_to_fahrenheit(100), float)
    assert isinstance(convert_to_fahrenheit(-40), float)

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


def test_minutes_to_clock():
    """minutes_to_clock - returns a string like '2h 5m' using // and %"""
    assert minutes_to_clock(125) == "2h 5m"
    assert minutes_to_clock(45) == "0h 45m"
    assert minutes_to_clock(60) == "1h 0m"
    assert minutes_to_clock(0) == "0h 0m"
    assert minutes_to_clock(1440) == "24h 0m"


def test_is_leap_year():
    """is_leap_year - divisible by 4, except by 100, unless also by 400"""
    assert is_leap_year(2024) is True
    assert is_leap_year(1996) is True
    assert is_leap_year(2000) is True
    assert is_leap_year(2023) is False
    assert is_leap_year(1900) is False
    assert is_leap_year(2100) is False


def test_make_banner():
    """make_banner - surrounds the text with three symbols on each side"""
    assert make_banner("Hi") == "*** Hi ***"
    assert make_banner("Hi", "=") == "=== Hi ==="
    assert make_banner("Hi", symbol="-") == "--- Hi ---"
    assert make_banner(text="Welcome", symbol="#") == "### Welcome ###"
    assert make_banner("") == "***  ***"


def test_calculate_room_cost():
    """calculate_room_cost - returns the area times the price per square foot"""
    assert calculate_room_cost(5, 3, 2) == 30
    assert calculate_room_cost(10, 7, 1.5) == 105
    assert calculate_room_cost(4, 4, 0) == 0
    assert calculate_room_cost(0, 8, 3) == 0


def test_is_vowel():
    """is_vowel - returns True for a, e, i, o, u in either case"""
    for letter in "aeiouAEIOU":
        assert is_vowel(letter) is True
    assert is_vowel("z") is False
    assert is_vowel("B") is False
    assert is_vowel("y") is False
