import os.path
from datetime import datetime

import pytest

from src.decorators import log


@pytest.mark.parametrize("arg_1, arg_2, expected_result", [(1, 0, " foo error: ZeroDivisionError. Inputs: (1, 0), {}"),
                                                           (1, 2, " foo ok")
                                                           ])
def test_log_decorator(arg_1, arg_2, expected_result):
    filename = 'test.txt'
    if os.path.exists(filename):
        os.remove(filename)

    @log(filename)
    def foo(x: int, y: int) -> float:
        return x / y

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    foo(arg_1, arg_2)

    with open(filename) as file:
        log_mess = file.read().strip()

    expected_log = now + expected_result

    assert log_mess == expected_log


@pytest.mark.parametrize("arg_1, arg_2, expected_result", [(1, 0, " foo error: ZeroDivisionError. Inputs: (1, 0), {}"),
                                                           (1, 2, " foo ok")
                                                           ])
def test_console_log(capsys, arg_1, arg_2, expected_result):
    @log()
    def foo(x: int, y: int) -> float:
        return x / y

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    foo(arg_1, arg_2)

    expected_log = now + expected_result

    log_mess = capsys.readouterr()

    assert log_mess.out.strip() == expected_log
