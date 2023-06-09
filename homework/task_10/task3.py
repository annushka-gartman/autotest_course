import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize('arg, result', [pytest.param((4, 2), 2, marks=pytest.mark.smoke),
                                         ((10, 9, 8, 7, 6, 5), 0.0006613756613756614),
                                         pytest.param((5, 0), 'infinity', marks=pytest.mark.skip('shit test')),
                                         ((5, -5), -1),
                                         ((5, 0.25), 20)
                                         ])
def test_division(arg, result):
    assert all_division(*arg) == result
