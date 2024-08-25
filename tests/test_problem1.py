from problem1.problem1 import is_leap_year
def test_is_leap_year():
    assert is_leap_year(2000)

def test_is_leap_year2():
    assert is_leap_year(2024)

def test_is_not_leap_year():
    assert not is_leap_year(2100)

def test_is_not_leap_year2():
    assert not is_leap_year(1999)

