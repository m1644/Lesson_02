import subprocess
import zlib


def run_command(cmd):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    return result.returncode, result.stdout, result.stderr


def is_command_successful(returncode, stdout, stderr, success_message):
    return returncode == 0 and success_message in stdout


def calculate_crc32(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
        crc32_value = zlib.crc32(data) & 0xFFFFFFFF
        return crc32_value

