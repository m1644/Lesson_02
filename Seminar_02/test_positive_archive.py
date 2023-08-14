import os
import pytest
from archiver_utils import run_command, is_command_successful


''' Задание 4
Доработать позитивные тесты таким образом, 
чтобы при архивации дополнительно проверялось создание файла архива, 
а при распаковке проверялось создание файлов.
'''

folder_in = "/home/user/tst"
folder_out = "/home/user/out"


def test_step_1():
    returncode, stdout, stderr = run_command(f"cd {folder_in}; 7z a {folder_out}/arh1.7z *")
    assert is_command_successful(returncode, stdout, stderr, "Everything is Ok") and os.path.exists(f"{folder_out}/arh1.7z"), 'Test_step_1 FAIL'


def test_step_2():
    returncode, stdout, stderr = run_command(f"cd {folder_in}; 7z u {folder_out}/arh1.7z *")
    assert is_command_successful(returncode, stdout, stderr, "Everything is Ok"), 'Test_step_2 FAIL'


def test_step_3():
    returncode, stdout, stderr = run_command(f"cd {folder_in}; 7z d {folder_out}/arh1.7z *")
    assert is_command_successful(returncode, stdout, stderr, "Everything is Ok"), 'Test_step_3 FAIL'


if __name__ == "__main__":
    pytest.main(["-v"])
