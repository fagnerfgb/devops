#Autor: Fagner Geraldes Braga  
#Data de criação: 13/12/2024  
#Data de atualização: 13/12/2024  
#Versão: 0.01

### namespace
```bash
unshare --pid --fork --mount-proc /bin/bash
```

```bash
ps -ef --forest
```

```bash
ps -aux
pwd
exit
```

### chroot
```bash
mkdir container
cd container
chroot .
ldd /bin/bash
```

```bash
apt update
apt install debootstrap -y
debootstrap jammy .
ls
ldd bin/bash
chroot .
ls /home
echo "teste" > teste.txt
exit
ls /root
ls root
```
```bash
chroot .
ps -aux
mount -t proc proc /proc
ps -aux
exit
```

### unshare e chroot
```bash
unshare --pid --fork --mount-proc chroot . /bin/bash
mount -t proc proc /proc
ps -aux
while true; do echo aula; done;
```

```bash
htop
```

### cgroup
```bash
ls /sys/fs/cgroup
echo "+cpu" >> /sys/fs/cgroup/cgroup.subtree_control
echo "+cpuset" >> /sys/fs/cgroup/cgroup.subtree_control
cd /sys/fs/cgroup
mkdir auladocker
cd aula docker
echo "+cpu" >> /sys/fs/cgroup/auladocker/cgroup.subtree_control
echo "+cpuset" >> /sys/fs/cgroup/auladocker/cgroup.subtree_control
# pegar pid do processo a ser gerenciado
echo "27528" >> /sys/fs/cgroup/auladocker/cgroup.procs
echo "0" >> /sys/fs/cgroup/auladocker/cpuset.cpus
echo "1" >> /sys/fs/cgroup/auladocker/cpuset.cpus
echo "500000 1000000" >> echo "0" >> /sys/fs/cgroup/auladocker/cpu.max
```
### LXC
```bash
apt update && apt install lxc lxc-templates -y
lxc-create -t ubuntu -n meucontainer
lxc-ls --fancy
lxc-start -n meucontainer
ps -ef --forest
lxc-attach -n meucontainer
ps -aux
```
### LXD
```bash
apt update && apt install lxd lxd-client -y
lxd init
lxc launch ubuntu:22.04 meucontainer
lxc list
lxc exec meucontainer -- bin/bash
ps -aux
lxc stop meucontainer
lxc delete meucontainer
```

### Docker Engine Install
https://docs.docker.com/engine/install/ubuntu/
```bash
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

sudo groupadd docker

sudo usermod -aG docker $USER
```