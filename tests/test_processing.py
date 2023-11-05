import pytest

from src.processing import get_list_dictionary_by_key, get_list_dictionaries_sorted


@pytest.fixture
def list_dictionary():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


def test_get_list_dictionary_by_key(list_dictionary):
    assert get_list_dictionary_by_key(list_dictionary) == [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ]


def test_get_list_dictionaries_sorted(list_dictionary):
    assert get_list_dictionaries_sorted(list_dictionary) == [{'id': 41428829, 'state': 'EXECUTED',
                                             'date': '2019-07-03T18:35:29.512364'},
                                            {'id': 615064591, 'state': 'CANCELED',
                                             'date': '2018-10-14T08:21:33.419441'},
                                            {'id': 594226727, 'state': 'CANCELED',
                                             'date': '2018-09-12T21:27:25.241689'},
                                            {'id': 939719570, 'state': 'EXECUTED',
                                             'date': '2018-06-30T02:08:58.425572'}]
