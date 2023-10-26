def get_mask_number_card(number: str) -> str:
    """Возвращает маску номера карты в формате XXXX XX** **** XXXX"""
    return number[:4] + " " + number[4:6] + "**" + " " + "****" + " " + number[-4:]


def get_mask_number_bill(number: str) -> str:
    """Возвращает маску номера счёта в формате **XXXX"""
    return "**" + number[-4:]
