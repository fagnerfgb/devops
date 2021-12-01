#!/bin/bash

#Atualizando o source list do apt
sudo apt update

#Atualizando todos os aplicativos (sistema)
sudo apt upgrade -y
sudo apt full-upgrade
sudo apt dist-upgrade

#Limpando todos os caches de aplicativos(sistema)
sudo apt autoremove
sudo apt autoclean

#Limpando todos os source list
sudo apt clean

#Hora do café
#sudo shutdown -h now


