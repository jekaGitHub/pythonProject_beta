from typing import Generator, Iterator


def filter_by_currency(transactions_list: list, currency: str) -> Iterator:
    """
    Принимает список словарей и возвращает итератор, выдающий по очереди операции с заданной валютой.
    :param transactions_list: список словарей
    :param currency: валюта, по которой нужно отфильтровать словари
    :return: generator, который выдаёт по очереди операции, в которых указана заданная валюта
    """
    return filter(lambda x: x["operationAmount"]["currency"]["code"] == currency, transactions_list)


def transaction_descriptions(transaction_list: list) -> Generator:
    """
    Генератор, который принимает список словарей и возвращает описание каждой операции по очереди.
    :param transaction_list: список словарей
    :return: итератор описания каждой операции по очереди
    """
    for item in transaction_list:
        yield item["description"]


def card_number_generator(start: int, stop: int) -> Generator:
    """
    Генератор номеров банковских карт, который должен генерировать номера карт в формате "XXXX XXXX XXXX XXXX",
    где X — цифра. Должны быть сгенерированы номера карт в заданном диапазоне, например, от 0000 0000 0000 0001
    до 9999 9999 9999 9999 (диапазоны передаются как параметры генератора).
    :param start: начальный диапазон номера банковской карты
    :param stop: конечный диапазон номера банковской карты
    :return: генерирует номера банковских карт
    """
    card_numbers = ((16 * "0")[0:-len(str(item))] + str(item) for item in range(start, stop + 1))
    for number in card_numbers:
        yield number[0:4] + " " + number[4:8] + " " + number[8:12] + " " + number[12:]
