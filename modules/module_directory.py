import subprocess


class Directory:

    path = None

    def __init__(self, path):
        self.path = path

    def create(self):
        cmd = "mkdir " + self.path
        stdout, stderr = self.bashCmd(cmd)
        return len(stderr) == 0

    def remove(self):
        cmd = "rm -rf " + self.path
        stdout, stderr = self.bashCmd(cmd)
        return len(stderr) == 0

    def change_owner(self, new_user, new_group):
        # change rigths
        new_owner = new_user
        if new_group is not None:
            new_owner = new_owner + ":" + new_group

        cmd_owner = "chown -R " + new_owner + " " + self.path
        stdout, stderr = self.bashCmd(cmd_owner)
        return len(stderr) == 0

    def change_permissions(self, permission):
        cmd = "chmod -R " + permission + " " + self.path
        stdout, stderr = self.bashCmd(cmd)
        return len(stderr) == 0

    def move(self, new_path):
        cmd = "mv " + self.path + " " + new_path
        self.path = new_path
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
