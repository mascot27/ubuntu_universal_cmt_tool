import subprocess
from modules import module_apache2


def activate_apache_mode(file_modes_list):
    mode_file = open(file_modes_list, 'r')

    mode_list_raw = mode_file.readlines()
    mode_list = []

    # to remove the line endings
    for mode in mode_list_raw:
        mode = mode[:len(mode) - 1]
        mode_list.append(mode)

    a = module_apache2.Apache2()
    for mode in mode_list:
        a.enable_apache2_mode(mode)


def activate_php_mode(file_modes_list):
    mode_file = open(file_modes_list, 'r')

    mode_list_raw = mode_file.readlines()
    mode_list = []

    # to remove the line endings
    for mode in mode_list_raw:
        mode = mode[:len(mode) - 1]
        mode_list.append(mode)

    a = module_apache2.Apache2()
    for mode in mode_list:
        a.enable_php_mode(mode)


def bashCmd(cmd):
    """
    Execute a bash command and return a stdout as string
    """
    completed = subprocess.run(cmd, shell=True, check=False, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    convertedOut = str(completed.stdout, 'utf-8')
    convertedErr = str(completed.stderr, 'utf-8')
    return convertedOut, convertedErr
