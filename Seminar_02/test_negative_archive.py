import pytest
from archiver_utils import run_command


''' Задание 3
Создать отдельный файл для негативных тестов. 
Функцию проверки вынести в отдельную библиотеку. 
Повредить архив (например, отредактировав его в текстовом редакторе). 
Написать негативные тесты работы архиватора с командами распаковки
(e) и проверки (t) поврежденного архива.
'''

folder_in = "/home/user/tst"
folder_out = "/home/user/out"


def test_extract_bad_archive():
    returncode, stdout, stderr = run_command(f"cd {folder_out}; 7z x {folder_out}/arh2.7z")
    assert returncode != 0, 'test_extract_bad_archive FAIL'


def test_bad_archive():
    returncode, stdout, stderr = run_command(f"cd {folder_out}; 7z t {folder_out}/arh2.7z")
    assert returncode != 0, 'test_bad_archive FAIL'


if __name__ == "__main__":
    pytest.main(["-v"])
