def get_mask_number_card(number: str) -> str:
    """ Возвращает маску номера карты в формате XXXX XX** **** XXXX

        :param number: номер карты
        :return: замаскированный номер карты
    """
    if len(number) != 16:
        return 'Некорректный номер. Введите номер снова.'
    return number[:4] + " " + number[4:6] + "**" + " " + "****" + " " + number[-4:]


def get_mask_number_bill(number: str) -> str:
    """ Возвращает маску номера счёта в формате **XXXX

        :param number: номер счёта
        :return: замаскированный номер счёта
    """

    if len(number) != 20:
        return 'Некорректный номер. Введите номер снова.'
    return "**" + number[-4:]
