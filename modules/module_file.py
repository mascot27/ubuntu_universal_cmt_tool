import subprocess


class File:

    path = None

    def __init__(self, path):
        self.path = path

    def move_to(self, path_new):
        cmd = "mv " + self.path + " " + path_new
        stdout, stderr = self.bashCmd(cmd)
        self.path = path_new
        return len(stderr) == 0

    def change_owner(self, user, group):
        cmd = "chown " + user + ":" + group + " " + self.path
        stdout, stderr = self.bashCmd(cmd)
        return len(stderr) == 0

    def change_permission(self, mode):
        cmd = "chmod " + mode + " " + self.path
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

