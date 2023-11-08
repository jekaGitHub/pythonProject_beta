import random
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


# def card_number_generator(start, stop):
#     while True:
#         yield random.randrange(start, stop)
