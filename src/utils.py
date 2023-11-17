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



if __name__ == '__main__':
    print(get_list_operations_from_json("../data/operations.json"))
