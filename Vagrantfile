# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.network "private_network", ip: "10.0.22.6"
  config.vm.provider "virtualbox" do |v|
    v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
    v.customize ["modifyvm", :id, "--natdnsproxy1", "on"]
    v.memory = 2048
    v.cpus = 2
  end
  config.vm.synced_folder ".", "/home/vagrant/octopeer"
  config.vm.provision "shell", path: "provision/bootstrap.sh", privileged: false
end
