# Octopeer

## Getting Started

1. The fastest way to set up the development environment is to install:

   * [VirtualBox](https://www.virtualbox.org/)
   * [Vagrant](https://www.vagrantup.com/)

1. Clone the Octopeer repository to the preferred location and change directory.
   Afterward, let Vagrant set up a fully running development box and SSH into it.

   ```bash
   host$ git clone git@github.com:theSorcerers/octopeer.git
   host$ cd octopeer
   host$ vagrant up
   host$ vagrant ssh
   ```

1. Perform a database migration and you are ready to go, fire up the server!

   ```bash
   vagrant$ rails db:migrate
   vagrant$ rails s -b 0.0.0.0
   ```

   You can access the application from the host machine at `10.0.22.6:3000`.
