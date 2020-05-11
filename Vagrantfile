# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
  config.vm.box = "ubuntu/trusty32"

  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # NOTE: This will enable public access to the opened port
  config.vm.network :forwarded_port, guest: 3306, host: 3306

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine and only allow access
  # via 127.0.0.1 to disable public access
  #config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
   config.vm.network "private_network", ip: "192.168.33.10"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  # config.vm.synced_folder "./scraper", "/scraper"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
   config.vm.provider "virtualbox" do |vb|
     # Display the VirtualBox GUI when booting the machine
     vb.gui = false

     # Customize the amount of memory on the VM:
     vb.memory = "2048"
   end
  #
  # View the documentation for the provider you are using for more
  # information on available options.

  # Enable provisioning with a shell script. Additional provisioners such as
  # Ansible, Chef, Docker, Puppet and Salt are also available. Please see the
  # documentation for more information about their specific syntax and use.
   config.vm.provision "shell", inline: <<-SHELL
          # Variables
          APPENV=local
          DBHOST=localhost
          DBNAME=ukcampsites
          DBUSER=pyscrape
          DBPASSWD=password

          echo -e "--- Updating packages list ---\n"
          apt-get update > /dev/null 2>&1

          echo -e "\n--- Install base packages ---\n"
          apt-get -y install vim curl build-essential software-properties-common python-software-properties > /dev/null 2>&1
          apt-get install zlib1g-dev git-core sqlite3 libsqlite3-dev  > /dev/null 2>&1

          echo -e "--- Install MySQL specific packages and settings ---\n"
          echo "mysql-server mysql-server/root_password password $DBPASSWD" | debconf-set-selections
          echo "mysql-server mysql-server/root_password_again password $DBPASSWD" | debconf-set-selections
          apt-get -y install mysql-server-5.5  > /dev/null 2>&1

          echo -e "--- Setting up our MySQL user and db ---\n"
          mysql -uroot -p$DBPASSWD -e "CREATE DATABASE $DBNAME" > /dev/null 2>&1
          mysql -uroot -p$DBPASSWD -e "grant all privileges on *.* to '$DBUSER'@'%' identified by '$DBPASSWD' WITH GRANT OPTION" > /dev/null 2>&1
          mysql -uroot -p$DBPASSWD -e "grant all privileges on *.* to 'vagrant'@'%' identified by '$DBPASSWD' WITH GRANT OPTION" > /dev/null 2>&1
          echo -e "--- SSH into MySQL as root and edit my.cnf changing bind-address 0.0.0.0 ---\n"

   SHELL
end
