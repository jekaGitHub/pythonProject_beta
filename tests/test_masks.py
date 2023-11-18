import pytest

from src.masks import get_mask_number_card, get_mask_number_bill


@pytest.mark.parametrize("number, expected", [("1234567834627910", "1234 56** **** 7910"),
                                              ("9876990045613477", "9876 99** **** 3477"),
                                              ("0055678932216996", "0055 67** **** 6996")
                                              ])
def test_get_mask_number_card(number, expected):
    assert get_mask_number_card(number) == expected


@pytest.mark.parametrize("number, expected", [("12345678346279109845", "**9845"),
                                              ("56789876990045613477", "**3477"),
                                              ("65670055678932214321", "**4321")
                                              ])
def test_get_mask_number_bill(number, expected):
    assert get_mask_number_bill(number) == expected


# @pytest.mark.parametrize("number, expected", [("", ""),
#                                               ("98769900456134", ""),
#                                               ("005567893221699689", "")
#                                               ])
def test_get_mask_number_card_incorrect():
    with pytest.raises(ValueError):
        get_mask_number_card("")


def test_get_mask_number_bill_incorrect():
    with pytest.raises(ValueError):
        get_mask_number_bill("")
