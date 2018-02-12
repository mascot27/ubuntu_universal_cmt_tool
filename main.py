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
password_mysql = "Qwertz123"
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

    # 5) local gen
    print("5) configuring locales")
    app_directShell.bashCmd("locale-gen fr_FR")
    app_directShell.bashCmd("locale-gen de_DE")

    # moves files

    f = module_file.File("ressources/toMove/files/id_rsa")
    f.move_to("root/.ssh/id_rsa")
    f.change_owner("root", "root")
    f.change_permission("0600")

    f = module_file.File("ressources/toMove/files/id_rsa.pub")
    f.move_to("root/.ssh/id_rsa.pub")
    f.change_owner("root", "root")
    f.change_permission("0644")

    f = module_file.File("ressources/toMove/files/php.ini")
    f.move_to("/etc/php/7.0/apache2/php.ini")

    f = module_file.File("ressources/toMove/files/vysual.conf")
    f.move_to("/etc/apache2/sites-available/vysual.conf")

    app_directShell.bashCmd("a2ensite vysual.conf")
    app_directShell.bashCmd("a2dissite 000-default.conf")

    f = module_file.File("ressources/toMove/files/ports.conf")
    f.move_to("/etc/apache2/ports.conf")

    f = module_file.File("ressources/toMove/files/apache2.conf")
    f.move_to("/etc/apache2/apache2.conf")

    f = module_file.File("ressources/toMove/files/apache2")
    f.move_to("/etc/logrotate.d/apache2")

    app_directShell.bashCmd("touch /opt/vysual/.secret/.htpasswd")
    f = module_file.File("/opt/vysual/.secret/.htpasswd")
    f.change_owner("root", "root")
    f.change_permission("0644")
    app_directShell.bashCmd("chmod +x /opt/vysual/.secret/.htpasswd")

    cmd = "htpasswd -b -c /opt/vysual/.secret/.htpasswd " + "virtual" + " " + password_mysql
    app_directShell.bashCmd(cmd)

    f = module_file.File("ressources/toMove/files/calibri.ttf")
    f.move_to("/usr/share/fonts/truetype/calibri.ttf")
    f = module_file.File("ressources/toMove/files/free3of9.ttf")
    f.move_to("/usr/share/fonts/truetype/free3of9.ttf")
    app_directShell.bashCmd("fc-cache -f -v")

    d = module_directory.Directory("ressources/toMove/directories/oracle")
    d.move("/opt/oracle/")
    cmd = "sh -c \"echo 'instantclient,/opt/oracle/instantclient' | pecl install oci8\""
    app_directShell.bashCmd(cmd)
    cmds = [
        "touch /etc/php/7.0/apache2/conf.d/20-oci.ini",
        "touch /etc/php/7.0/cli/conf.d/20-oci.ini",
        "echo \"extension=oci8.so\" >> /etc/php/7.0/apache2/conf.d/20-oci.ini",
        "echo \"extension=oci8.so\" >> /etc/php/7.0/cli/conf.d/20-oci.ini"
    ]
    for cmd in cmds:
        app_directShell.bashCmd(cmd)

    f = module_file.File("ressources/toMove/files/supervisord.conf")
    f.move_to("/etc/supervisor/supervisord.conf")

    f = module_file.File("ressources/toMove/files/ntp.conf")
    f.move_to("/etc/ntp.conf")

    cmds = [
        "curl -sS https://getcomposer.org/installer -o composer-setup.php",
        "php composer-setup.php --install-dir=/usr/local/bin --filename=composer"
    ]
    for cmd in cmds:
        app_directShell.bashCmd(cmd)

    app_directShell.bashCmd("reboot")
