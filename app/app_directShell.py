import subprocess


def bashCmd(cmd):
    """
    Execute a bash command and return a stdout as string
    """
    completed = subprocess.run(cmd, shell=True, check=False, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    convertedOut = str(completed.stdout, 'utf-8')
    convertedErr = str(completed.stderr, 'utf-8')
    return convertedOut

