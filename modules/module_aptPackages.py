import subprocess

cmd = "apt-cache policy"


class AptPackages:
    name = None
    isAvailable = None
    isInstalled = None

    def __init__(self, name):
        self.name = name

    def is_package_available(self):
        to_exec = cmd + " " + str(self.name)
        stdout, stderr = self.bashCmd(to_exec)
        stdout_processed = stdout.splitlines()

        if not stdout_processed:
            return False

        return True

    def is_package_installed(self):
        to_exec = cmd + " " + str(self.name)
        stdout, stderr = self.bashCmd(to_exec)
        stdout_processed = stdout.splitlines()

        if len(stderr) > 0:
            return False

        if not stdout_processed:
            return False

        if "none" in stdout_processed[1]:
            return False

        return True

    def install_package(self):
        to_exec = "apt-get install -y " + self.name
        stdout, stderr = self.bashCmd(to_exec)

        return len(stderr) == 0

    def bashCmd(self, cmd):
        """
        Execute a bash command and return a stdout as string
        """
        completed = subprocess.run(cmd, shell=True, check=False, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        converted_out = str(completed.stdout, 'utf-8')
        converted_err = str(completed.stderr, 'utf-8')
        return converted_out, converted_err
