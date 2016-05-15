# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.network "private_network", ip: "10.0.22.6"
  config.vm.provider "virtualbox" do |v|
    v.customize ["modifyvm", :id, "--nictype1", "virtio"]
  end
  config.vm.synced_folder ".", "/home/vagrant/octopeer"
  config.vm.provision "shell", path: "bootstrap.sh", privileged: false
end
