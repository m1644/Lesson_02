import subprocess
import pytest


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False


def test_step_1():
    # Test_01
    assert checkout("cd /home/user/tst; 7z a ../out/arx2", "Everything is Ok"), 'Test_01 FAIL'


@pytest.mark.run_this
def test_step_2():
    # Test_02
    assert checkout("cd /home/user/out; 7z e arx2.7z -o/home/user/folder1 -y", "Everything is Ok"), 'Test_02 FAIL'


def test_step_3():
    # Test_03
    assert checkout("cd /home/user/out; 7z t arx2.7z", "Everything is Ok"), 'Test_03 FAIL'
