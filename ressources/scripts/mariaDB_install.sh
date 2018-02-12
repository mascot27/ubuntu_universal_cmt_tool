#!/usr/bin/env bash

mariadbPassword=$1

# install mariadb in an automated way
apt-get -y install software-properties-common
apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xF1656F24C74CD1D8
add-apt-repository 'deb [arch=amd64,i386,ppc64el] http://ftp.heanet.ie/mirrors/mariadb/repo/10.2/ubuntu xenial main'
apt-get -y update

export DEBIAN_FRONTEND=noninteractive
debconf-set-selections <<< "mariadb-server mysql-server/root_password password $mariadbPassword"
debconf-set-selections <<< "mariadb-server mysql-server/root_password_again password $mariadbPassword"
apt-get -y install mariadb-server
export DEBIAN_FRONTEND=dialog

apt-get -y install mariadb-plugin-connect
