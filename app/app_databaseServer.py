from modules import module_mariaDB


def install(password, script_file_install, script_file_user, cmd_list_file, new_config):
    server = module_mariaDB.MariaDbServer(password)
    server.install_mariadb(script_file_install)
    server.install_users(script_file_user)
    server.execute_all_command_from_file(cmd_list_file)
    server.replace_configuration_file(new_config)
