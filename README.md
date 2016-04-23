# Octopeer

## Getting Started

1. The fastest way to set up the development environment is to install:

    * [VirtualBox](https://www.virtualbox.org/)
    * [Vagrant](https://www.vagrantup.com/)

1. Clone the Octopeer repository to the preferred location and change directory.
Afterwards, let Vagrant set up a fully running development box and SSH into it.
(Do this on the host machine, this setup will create a virtual machine itself.)
When you're using windows, try installing git and running the following commands from Git Bash as 
```bash
host$ vagrant ssh
```
may not work in cmd.

   ```bash
   host$ git clone git@github.com:theSorcerers/octopeer.git
   host$ cd octopeer
   host$ vagrant up
   host$ vagrant ssh
   ```
1. Go to the project directory, and initialize and activate [virtualenv](https://virtualenv.pypa.io/en/latest/).
Then, install all dependencies with [pip](https://pip.pypa.io/en/stable/).

   ```bash
   vagrant$ cd octopeer
   vagrant$ virtualenv -p python3 env
   vagrant$ source env/bin/activate
   vagrant$ pip install -r requirements.txt
   ```

1. You are ready to start hacking, fire up the server!

   ```bash
   vagrant$ python manage.py runserver 0.0.0.0:8000
   ```

   You can access the application from the host machine at `localhost:8000`.

1. **OPTIONAL**: If `localhost` gets boring, you can modify it in your host file.

   ```bash
   host$ echo '192.168.22.6 octopeer.app' | sudo tee --append /etc/hosts
   ```
   You can now access the application from the host machine at `octopeer.app:8000`.
