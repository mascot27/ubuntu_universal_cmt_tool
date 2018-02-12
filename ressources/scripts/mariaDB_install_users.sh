#!/usr/bin/env bash

mariaDBPassword=$1

mysql -e "UPDATE mysql.user SET Password = PASSWORD('$mariaDBPassword') WHERE User = 'root';"
# Kill off the demo database
mysql -e "DROP DATABASE test;"
# using magic command right here:
mysql -D mysql -e "UPDATE user SET plugin='mysql_native_password' WHERE User='root';"
# just flush that shit
mysql -e "FLUSH PRIVILEGES;"
mysql -e "EXIT"
# Any subsequent tries to run queries this way will get access denied because lack of usr/pwd param

# Create user 'view'
mysql -u root -p${mariaDBPassword} -e "CREATE USER 'view'@'localhost' IDENTIFIED BY '$mariaDBPassword';"
# Grant SELECT privileges on vysual database
mysql -u root -p${mariaDBPassword} -e "GRANT SELECT ON vysual.* TO 'view'@'localhost';"
# Make our changes take effect
mysql -u root -p${mariaDBPassword} -e "FLUSH PRIVILEGES"
mysql -u root -p${mariaDBPassword} -e "EXIT"
