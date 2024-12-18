#Autor: Fagner Geraldes Braga  
#Data de criação: 12/12/2024  
#Data de atualização: 12/12/2024  
#Versão: 0.01

```bash
uname
uname -s
uname -n
uname -r
uname -v
uname -m
uname -p
uname -i
uname -o
uname -a
```
```bash
who
free
```
```bash
pwd
cd
cd ..
ls
ls -a
ls -l
ls -la
mkdir
mkdir -p
rm -rf
cp
mv
touch
cat
head
head -n 2
tail
tail -n 2
more
less
grep -n
grep -i
```
```bash
ls -l | grep erro
ls -l > saida.txt
ls -l >> saida.txt
mkdir fagner/teste 2> erro.txt
mkdir fagner/teste 2> /dev/null
```
```bash
ls -a /dev
mkdir -p /mnt/hd
mount /dev/sda1 /mnt/hd 
umount /mnt/hd
```
```bash
dpkg -i
dpkg -r
apt update
apt upgrade
apt install
apt remove
apt search
```
```bash
ps
ps -a
ps -ax
ps -aux
kill
top
htop
```
```bash
ssh user@endereço

ssh-keygen -t rsa -b 2048 
cat ~/.ssh/id_rsa.pub
ssh -i ~/.ssh/id_rsa user@endereço
```
