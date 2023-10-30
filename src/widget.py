import datetime
from src.masks import get_mask_number_card, get_mask_number_bill


def get_mask_deposit(deposit: str) -> str:
    """ принимает на вход строку с информацией тип карты/счета и номер карты/счета
        возвращает эту строку с замаскированным номером карты/счета.

        :param deposit: строка с название карты/счета и номером карты/счета
        :return: строка с маскированным по правилу номером карты/счета
    """

    # список, полученный из строки, переданной в функцию
    deposit_list = deposit.strip().split()

    if deposit_list[0].startswith('Счет'):
        return deposit_list[0] + ' ' + get_mask_number_bill(deposit_list[1])
    elif len(deposit_list) == 2 and not deposit_list[0].startswith('Счет'):
        return deposit_list[0] + ' ' + get_mask_number_card(deposit_list[1])
    else:
        return deposit_list[0] + ' ' + deposit_list[1] + ' ' + get_mask_number_card(deposit_list[2])

# тестирование функции get_mask_deposit()
# print(get_mask_deposit('Maestro 1596837868705199'))
# print(get_mask_deposit('Счет 64686473678894779589'))
# print(get_mask_deposit('MasterCard 7158300734726758'))
# print(get_mask_deposit('Счет 35383033474447895560'))
# print(get_mask_deposit('Visa Classic 6831982476737658'))
# print(get_mask_deposit('Visa Platinum 8990922113665229'))
# print(get_mask_deposit('Visa Gold 5999414228426353'))
# print(get_mask_deposit('Счет 73654108430135874305'))


def get_date_formatting(str_date: str) -> str:
    """ Функция преобразования строки с датой в строку формата дд.мм.гггг

        :param str_date: строка, содержащая дату
        :return: строка с датой в виде "дд.мм.гггг"
    """

    return datetime.datetime.strptime(str_date, '%Y-%m-%d %H:%M:%S.%f').strftime('%d.%m.%Y')


# тестирование функции get_date_formatting()
print(get_date_formatting('2018-07-11 02:26:18.671407'))
