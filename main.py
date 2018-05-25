from app import app_packageInstall
from app import app_creationDossier
from app import app_directShell
from app import app_webserverApache2
from app import app_databaseServer
from modules import module_file
from modules import module_directory

# apt
packageListFile = "ressources/aptList.txt"
# filesystem
dossiers = "ressources/dossiers.json"
# apache
apache_modes = "ressources/apache2ModesList.txt"
# php
php_modes = "ressources/phpModesList.txt"
# mysql
password_mysql = "Hunter2"
mysql_script_install = "ressources/scripts/mariaDB_install.sh"
mysql_script_user = "ressources/scripts/mariaDB_install_users.sh"
mysql_command_list = "ressources/mySqlCommandeList.txt"
mysql_config = "ressources/toMove/files/my.cnf"

if __name__ == '__main__':
    print("welcome on CMT TOOL")
    # 1) install provided packages
    print("1) installing packages")
    print("----------------------")
    app_packageInstall.install_all_packages(packageListFile)
    print("----------------------")
    # 2) prepare directories
    print("2) preparing directories")
    print("----------------------")
    app_creationDossier.create_all_directories(dossiers)
    print("----------------------")
    # 3) apache configuration
    print("3) configuring apache2")
    app_webserverApache2.activate_apache_mode(apache_modes)
    app_webserverApache2.activate_php_mode(php_modes)

    # 4) mariaDB configuration
    print("4) configuring mariadb")
    app_databaseServer.install(password_mysql, mysql_script_install, mysql_script_user, mysql_command_list, mysql_config)

    # moves files

    f = module_file.File("ressources/toMove/files/fileExample")
    f.move_to("root/dumb/id_rsa")
    f.change_owner("root", "root")
    f.change_permission("0600")

    app_directShell.bashCmd("echo 'command here'")
    
    
    
    cmd = "echo 'great'"
    app_directShell.bashCmd(cmd)

    d = module_directory.Directory("ressources/toMove/directories/exempleDir")
    d.move("/opt/exemple/")
    
    cmds = [
        "echo '1'",
        "echo '2'",
        "echo '3'"]
    for cmd in cmds:
        app_directShell.bashCmd(cmd)

    app_directShell.bashCmd("reboot")
