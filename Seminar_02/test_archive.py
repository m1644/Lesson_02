import subprocess
import pytest


''' Задание 1
Установить пакет pip3, выполнив в терминале команду:
sudo apt install python3-pip
Установить пакет pytest командой:
sudo pip3 install pytest
Установить консольный архиватор командой:
sudo apt install p7zip-full
'''

''' Задание 2
Добавить в проект тесты, проверяющие работу команд d (удаление из архива) и u (обновление архива). 
Вынести в отдельные переменные пути к папкам с файлами, с архивом и с распакованными файлами. 
Выполнить тесты с ключом -v.
'''

def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False


folder_in = "/home/user/tst"
folder_out = "/home/user/out"


def test_step_1():
    # Test_01
    assert checkout(f"cd {folder_in}; 7z a {folder_out}/arh1", "Everything is Ok"), 'Test_01 FAIL'


def test_step_2():
    # Test_02
    assert checkout(f"cd {folder_in}; 7z u {folder_out}/arh1", "Everything is Ok"), 'Test_02 FAIL'


def test_step_3():
    # Test_03
    assert checkout(f"cd {folder_in}; 7z d {folder_out}/arh1", "Everything is Ok"), 'Test_03 FAIL'


if __name__ == "__main__":
    pytest.main(["-v"])
