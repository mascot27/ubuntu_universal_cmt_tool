from modules import module_aptPackages
import subprocess


def install_all_packages(package_list_file, max_try=3):
    # update system
    bashCmd("apt-get -y update")
    bashCmd("apt-get -y dist-upgrade")
    bashCmd("apt-get -y autoremove")

    # read file and extract packages as an array
    package_file = open(package_list_file, 'r')

    packages_list_raw = package_file.readlines()
    package_list = []

    # to remove the line endings
    for package in packages_list_raw:
        package = package[:len(package) - 1]
        package_list.append(package)

    # now package_list contain all the packages as
    # an string array
    t = 0
    while t <= max_try:
        list_package_already_installed = []
        list_package_not_found = []
        list_package_to_install = []

        # for each packages create an object to check if
        # can be installed or need to be installed
        for package in package_list:
            apt = module_aptPackages.AptPackages(package)
            available = apt.is_package_available()
            isInstalled = apt.is_package_installed()

            if not available:
                list_package_not_found.append(apt)
            elif isInstalled:
                list_package_already_installed.append(apt)
            else:
                list_package_to_install.append(apt)

        # process to installation
        list_package_install_success = []
        list_package_install_fail = []
        for package in list_package_to_install:
            success = package.install_package()
            if success:
                list_package_install_success.append(package)
            else:
                list_package_install_fail.append(package)

        if len(list_package_install_fail) == 0:
            t = max_try + 1


    # result
    print("result")
    print(package_list)
    print("installed : ")
    print_package_list(list_package_already_installed)
    print("not found: ")
    print_package_list(list_package_not_found)
    print("fail:")
    print_package_list(list_package_install_fail)


def print_package_list(aptlist):
    for package in aptlist:
        print(package.name)


def bashCmd(cmd):
    """
    Execute a bash command and return a stdout as string
    """
    completed = subprocess.run(cmd, shell=True, check=False, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    convertedOut = str(completed.stdout, 'utf-8')
    convertedErr = str(completed.stderr, 'utf-8')
    return convertedOut
