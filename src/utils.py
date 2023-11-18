import json


def get_list_operations_from_json(datafile: str) -> list:
    """Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.

    :param datafile: путь к файлу json
    :return: list, который содержит словари с данными о транзакциях
    """
    try:
        with open(datafile, encoding='utf-8') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                print('Ошибка при преобразовании в JSON данных из файла.')
                return []
    except FileNotFoundError:
        print(f'Файл {datafile} не найден.')
        return []

    return data


def get_amount_transaction_in_rub(transaction: dict) -> float:
    """Принимает на вход одну транзакцию и сумму транзакции в рублях, или ошибку, если не в рублях.

    param: transaction: одна транзакция
    :return: сумму транзакции или ошибку с сообщением 'Транзация выполнена не в рублях. Укажите транзакцию в рублях'
    """

    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        amount = transaction["operationAmount"]["amount"]
    else:
        raise ValueError("Транзация выполнена не в рублях. Укажите транзакцию в рублях")
    return amount


if __name__ == '__main__':
    # print(get_list_operations_from_json("../data/operations.json"))

    # проверка функции get_amount_transaction_in_rub
    transactions = get_list_operations_from_json("../data/operations.json")

    for item in transactions:
        print(get_amount_transaction_in_rub(item))
