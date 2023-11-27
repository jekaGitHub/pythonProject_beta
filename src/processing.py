import re
from collections import Counter


def get_list_dictionary_by_key(list_dictionaries: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """
    Функция принимает на вход список словарей и значение для ключа "state" и возвращает список,
    содержащий только те словари, у которых ключ state содержит переданное в функцию значение.
    :param list_dictionaries: список словарей
    :param state: значение для ключа state, по умолчанию = EXECUTED
    :return: список словарей, содержащий ключ со значением аргумента state
    """
    result_list = [item for item in list_dictionaries if item['state'] == state]
    return result_list


def get_list_dictionaries_sorted(list_dictionaries: list[dict], sort_order: bool = True) -> list[dict]:
    """
    Функция принимает на вход список словарей и возвращает новый список, в котором исходные словари отсортированы
    по убыванию даты (ключ date). Функция принимает два аргумента, второй необязательный задает порядок сортировки
    (убывание, возрастание)
    :param list_dictionaries: список словарей
    :param sort_order: порядок сортировки, по умолчанию = True
    :return: список отсортированных словарей
    """
    sorted_dictionaries = sorted(list_dictionaries, key=lambda dictionary: dictionary['date'], reverse=sort_order)
    return sorted_dictionaries


def get_transactions_by_str_filter(list_dictionaries: list[dict], str_filter: str) -> list[dict]:
    """
    Функция, которая будет принимать список словарей с данными о банковских операциях и строку поиска и возвращать список словарей, у которых в описании есть данная строка.
    :param list_dictionaries: список словарей
    :param str_filter: строка поиска
    :return: список словарей, у которых есть строка поиска
    """
    list_result = []
    pattern = re.compile(r'\b' + str_filter + r'\b')

    for item in list_dictionaries:
        try:
            if re.search(pattern, item['description']) is None:
                continue
            else:
                list_result.append(item)

        except KeyError:
            continue
    return list_result


def get_categories_and_count_operations(list_dictionaries: list[dict], categories: dict) -> dict:
    """
    Функция, которая будет принимать список словарей с данными о банковских операциях и словарь категорий операций
    и возвращать словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой
    категории.
    :param list_dictionaries: список словарей
    :param categories: словарь категорий
    :return: словарь вида {"category": count}
    """
    counter = Counter(item['description'] for item in list_dictionaries)
    categories.update(counter)

    return categories
