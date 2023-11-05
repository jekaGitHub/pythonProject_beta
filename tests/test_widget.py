import pytest

from src.widget import get_mask_deposit, get_date_formatting


@pytest.mark.parametrize("deposit, expected", [("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
                                               ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
                                               ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
                                               ("Счет 64686473678894779589", "Счет **9589")
                                               ])
def test_get_mask_deposit(deposit, expected):
    assert get_mask_deposit(deposit) == expected
