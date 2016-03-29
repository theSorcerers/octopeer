# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.network "forwarded_port", guest: 8000, host: 8000, auto_correct: true
  config.vm.network "private_network", ip: "192.168.22.6"
  config.vm.synced_folder "/home/aaronang/Code", "/home/vagrant/Code"
  config.vm.provision "shell", path: "bootstrap.sh"
end
