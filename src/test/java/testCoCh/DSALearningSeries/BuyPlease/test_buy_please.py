import pytest
from src.main.java.testCoCh.DSALearningSeries.BuyPlease.buy_please \
    import buy_please


test_data = [
    (2, 4, 4, 5, 28),
    (1, 1, 4, 8, 12)
]


@pytest.mark.parametrize("a,b,x,y,expected_result", test_data)
def test_buy_please(a: int, b: int, x: int, y: int, expected_result: int):
    assert expected_result == buy_please(a, b, x, y)
