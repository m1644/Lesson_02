import subprocess


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    # Test_01
    if checkout("cd /home/user/tst; 7z a ../out/arx2", "Everything is Ok"):
        print('Test_01 SUCCESS')
    else:
        print('Test_01 FAIL')
    # Test_02
    if checkout("cd /home/user/out; 7z e arx2.7z -o/home/user/folder1 -y", "Everything is Ok"):
        print('Test_02 SUCCESS')
    else:
        print('Test_02 FAIL')
    # Test_03
    if checkout("cd /home/user/out; 7z t arx2.7z", "Everything is Ok"):
        print('Test_03 SUCCESS')
    else:
        print('Test_03 FAIL')
