import os
import pytest
from archiver_utils import run_command, is_command_successful

''' Задание 1
Дополнить проект тестами, проверяющими команды вывода списка
файлов (l) и разархивирования с путями (x).
'''

folder_in = "/home/user/tst"
folder_out = "/home/user/out"


def test_step_1():
    returncode, stdout, stderr = run_command(f"cd {folder_in}; 7z a {folder_out}/arh1.7z *")
    assert is_command_successful(returncode, stdout, stderr, "Everything is Ok") and os.path.exists(
        f"{folder_out}/arh1.7z"), 'Test_step_1 FAIL'


def test_step_2():
    returncode, stdout, stderr = run_command(f"cd {folder_in}; 7z u {folder_out}/arh1.7z *")
    assert is_command_successful(returncode, stdout, stderr, "Everything is Ok"), 'Test_step_2 FAIL'


def test_step_3():
    returncode, stdout, stderr = run_command(f"cd {folder_in}; 7z d {folder_out}/arh1.7z *")
    assert is_command_successful(returncode, stdout, stderr, "Everything is Ok"), 'Test_step_3 FAIL'


def test_step_4():
    returncode, stdout, stderr = run_command(f"7z l {folder_out}/arh1.7z")
    assert is_command_successful(returncode, stdout, stderr,
                                 f"Listing archive: {folder_out}/arh1.7z"), 'Test_step_4 FAIL'


def test_step_5():
    returncode, stdout, stderr = run_command(f"7z x {folder_out}/arh1.7z -o{folder_out}")
    assert is_command_successful(returncode, stdout, stderr, "Everything is Ok"), 'Test_step_5 FAIL'


if __name__ == "__main__":
    pytest.main(["-v"])
