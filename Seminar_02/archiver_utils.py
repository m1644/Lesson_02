import subprocess


def run_command(cmd):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    return result.returncode, result.stdout, result.stderr


def is_command_successful(returncode, stdout, stderr, success_message):
    return returncode == 0 and success_message in stdout
