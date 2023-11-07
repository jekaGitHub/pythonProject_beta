def get_list_dictionary_by_key(list_dictionaries: list, state: str = 'EXECUTED') -> list:
    """
    Функция принимает на вход список словарей и значение для ключа "state" и возвращает список,
    содержащий только те словари, у которых ключ state содержит переданное в функцию значение.
    :param list_dictionaries: список словарей
    :param state: значение для ключа state, по умолчанию = EXECUTED
    :return: список словарей, содержащий ключ со значением аргумента state
    """
    result_list = [item for item in list_dictionaries if item['state'] == state]
    return result_list


def get_list_dictionaries_sorted(list_dictionaries: list, sort_order: bool = True) -> list:
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

