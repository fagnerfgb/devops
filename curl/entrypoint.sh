#!/bin/bash

if [ -z $1 ]
then
    echo "Iniciando o container sem parametro"
else
    echo "Iniciando o container com o parametro $1"
fi