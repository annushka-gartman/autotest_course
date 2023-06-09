import pytest

TEST_DATA = [
    (4, 2),
    (10, 9, 8, 7, 6, 5),
    (5, 0),
    (5, -5),
    (5, 0.25)
]


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.smoke
def test_simple_division():
    assert all_division(*TEST_DATA[0]) == 2


@pytest.mark.smoke
def test_multi_division():
    assert all_division(*TEST_DATA[1]) == 0.0006613756613756614


def test_division_zero():
    with pytest.raises(ZeroDivisionError):
        all_division(*TEST_DATA[2])


def test_negative_number():
    assert all_division(*TEST_DATA[3]) == -1


@pytest.mark.kiska
def test_fractional_number():
    assert all_division(*TEST_DATA[4]) == 20
