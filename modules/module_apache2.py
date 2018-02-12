import subprocess


class Apache2:

    folder = None

    def __init__(self):
        pass

    def enable_apache2_mode(self, mode_name):
        cmd = "a2enmode " + mode_name
        stdout, stderr = self.bashCmd(cmd)
        return len(stderr) == 0

    def enable_php_mode(self, mode_name):
        cmd = "phpenmode " + mode_name
        stdout, stderr = self.bashCmd(cmd)
        return len(stderr) == 0

    def bashCmd(self, cmd):
        """
        Execute a bash command and return a stdout as string
        """
        completed = subprocess.run(cmd, shell=True, check=False, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        converted_out = str(completed.stdout, 'utf-8')
        converted_err = str(completed.stderr, 'utf-8')
        return converted_out, converted_err
