import subprocess


class MariaDbServer:

    password_root = None

    def __init__(self, password):
        self.password_root = password

    def install_mariadb(self, script_file):
        cmd = "bash " + script_file + " " + self.password_root
        stdout, stderr = self.bashCmd(cmd)
        return len(stderr) == 0

    def install_users(self, script_file):
        cmd = "bash " + script_file + " " + self.password_root
        stdout, stderr = self.bashCmd(cmd)
        return len(stderr) == 0

    def execute_all_command_from_file(self, command_list_file):
        command_file = open(command_list_file, 'r')

        command_list_raw = command_file.readlines()
        command_list = []

        # to remove the line endings
        for cmd in command_list_raw:
            cmd = cmd[:len(cmd) - 1]
            command_list.append(cmd)

        cmd_base = "mysql -u root -p" + self.password_root + " -e "

        for cmd in command_list:
            execute_me = cmd_base + cmd
            self.bashCmd(execute_me)

    def replace_configuration_file(self, new_config_path):
        cmd = "mv " + new_config_path + " /etc/mysql/my.cnf"
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

