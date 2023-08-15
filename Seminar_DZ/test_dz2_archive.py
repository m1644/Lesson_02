import os
import pytest
from archiver_utils import run_command, is_command_successful, calculate_crc32


''' Задание 2
Установить пакет для расчета crc32:
sudo apt install libarchive-zip-perl
Доработать проект, добавив тест команды расчета хеша (h). 
Проверить, что хеш совпадает с рассчитанным командой crc32.
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


def test_calculate_crc32():
    test_file_path = f"{folder_in}/file1.txt"
    expected_crc32 = calculate_crc32(test_file_path)
    returncode, stdout, stderr = run_command(f"7z h {test_file_path}")
    assert is_command_successful(returncode, stdout, stderr, "CRC32  for data:"), 'Test_calculate_crc32 FAIL'
    lines = stdout.strip().split('\n')
    crc32_line = [line for line in lines if line.startswith("CRC32  for data:")][0]
    crc32_actual = int(crc32_line.split()[-1], 16)
    assert crc32_actual == expected_crc32, 'Test_calculate_crc32 FAIL'


if __name__ == "__main__":
    pytest.main(["-v"])
