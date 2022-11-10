from utils import sum_odd_position
import pytest


@pytest.mark.parametrize('a, expected_result', [(['4', '3', '2', '1', '2', '1', '6'], 5),
(['4', '1', '2', '5', '2', '7', '6'], 13),
(['4', '9', '2', '0', '2', '2', '6'], 11),
(['4', '2', '2', '4', '2', '0', '6'], 5),
(['4', '8', '2', '7', '2', '6', '6'], 21)])


def test_sum_odd_position_good(a, expected_result):
    assert sum_odd_position(a) == expected_result