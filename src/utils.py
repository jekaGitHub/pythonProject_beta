import json
import os
import csv

import pandas as pd

from src.logger import setup_logging

logger = setup_logging("utils.py")


def get_list_operations_from_json(datafile: str) -> list:
    """Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.

    :param datafile: путь к файлу json
    :return: list, который содержит словари с данными о транзакциях
    """
    try:
        with open(datafile, encoding='utf-8') as f:
            try:
                data: list = json.load(f)
            except json.JSONDecodeError:
                print('Ошибка при преобразовании в JSON данных из файла.')
                logger.error('Ошибка при преобразовании данных в JSON')
                return []
    except FileNotFoundError:
        print(f'Файл {datafile} не найден.')
        logger.error('Файл не найден')
        return []
    logger.info(f"Данные о финансовых транзакциях успешно получены из файла {os.getcwd()}\\{datafile}")
    return data


def get_amount_transaction_in_rub(transaction: dict) -> float:
    """Принимает на вход одну транзакцию и сумму транзакции в рублях, или ошибку, если не в рублях.

    param: transaction: одна транзакция
    :return: сумму транзакции или ошибку с сообщением 'Транзация выполнена не в рублях. Укажите транзакцию в рублях'
    """
    logger.debug('Происходит проверка транзакции')

    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        amount = transaction["operationAmount"]["amount"]
        logger.info('Транзакция проверена и получена сумма транзакции в рублях')
    else:
        logger.error("Ошибка! Транзакция не в рублях.")
        raise ValueError("Транзация выполнена не в рублях. Укажите транзакцию в рублях")
    return float(amount)


def get_transactions_from_csv(csv_file: str):
    with open(csv_file) as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            print(row)


def get_transactions_from_xlsx(xlsx_file: str):
    return pd.read_excel(xlsx_file, index_col=0)


if __name__ == '__main__':
    # print(get_list_operations_from_json("../data/operations.json"))
    #
    # # проверка функции get_amount_transaction_in_rub
    # transactions = get_list_operations_from_json("../data/operations.json")
    #
    # for item in transactions:
    #     print(get_amount_transaction_in_rub(item))


    # проверка загрузки xlsx файла
    xlsx_transactions = get_transactions_from_xlsx("../data/transactions_excel.xlsx")
    print(xlsx_transactions.head())
    print(xlsx_transactions.shape)
