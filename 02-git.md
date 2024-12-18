#Autor: Fagner Geraldes Braga  
#Data de criação: 11/12/2024  
#Data de atualização: 12/12/2024  
#Versão: 0.02

```git
git config --list
```
```git
git config --global user.name "Fagner Geraldes Braga"
git config --global user.email fagner.fgb@gmail.com
git config --global core.editor "code --wait"
git config --global init.defaultbranch main
```
```git
git init
git status
git add nome-do-arquivo
git add .
git reset
git commit
git commit -m "Comentário"
git commit -am "Comentário"
```
```git
git log
git log -p "nome-do-arquivo"
```
```git
git checkout hash
git checkout main
```
```git
git reset --soft HEAD~1
git reset --hard
```

```git
mkdir bin
touch bin/teste.exe
echo "teste" >> dados.log
```

```git
vim .gitignore
bin/
*.log
```

```git
git branch feature/novo_arquivo
git branch
git checkout feature/novo_arquivo
echo "Corinthians" >> arquivo.txt
git commit -am "primeiro commit na nova branch"
git checkout main
cat arquivo.txt
```

```git
git branch -m feature/fagner
```

```git
git checkout main
git branch -d feature/fagner
git branch -D feature/fagner
```

```git
git checkout -b feature/fagner
echo "branch feature/fagner" >> fagner.txt
git add .
git commit -m "adicionando o arquivo fagner.txt"
git checkout main
echo "Natalia da Paz Almeida" >> arquivo.txt
git commit -am "alterando o arquivo.txt"
git checkout feature/fagner
cat arquivo.txt
git checkout main
git merge feature/fagner
git branch -d feature/fagner
```

```git
git checkout -b feature/fagner_rebase
echo "Adicionando o arquivo rebase.txt" >> rebase.txt
git add . 
git commit -m "adicionando o arquivo rebase.txt"

git checkout main
echo "Adicionando arquivo main.txt" >> main.txt
git add . 
git commit -m "adicionando o arquivo main.txt"

git checkout feature/fagner_rebase
echo "Nova linha no arquivo rebase.txt" >> rebase.txt
git add . 
git commit -m "adicionando o arquivo rebase.txt"

git checkout main
git rebase feature/fagner_rebase

git branch -d feature/fagner_rebase
```

```git
git checkout -b feature/fagner_cherry_pic
echo "Primeira linha" >> cherrypic.txt
git add .
git commit -m "adicionando arquivo cherrypic.txt"
git checkout main

git checkout -b hotfix
echo "Hotfix" >> hotfix.txt
git add .
git commit -m "adicionando arquivo hotfix.txt"
git log
git checkout feature/fagner_cherry_pic
git cherry-pick bad9619ca8056998e8fa3af0670c2b56bd05a5f0
git checkout main
```

```git
git tag
git tag -a v2.0 -m "Versão 2.0"
git tag -a v1.0 -m "Versão 1.0" 8311b997cf0c707f526a51191708d1c7be3696cc
git tag
git show v1.0
git show v2.0
git tag -d v2.0
```
```git
# Criando chave SSH

ssh-keygen -t rsa -b 2048
cat id_rsa.pub
```
```git
git remote add origin git@github.com:fagnerfgb/devops.git
git branch -M master
git push -u origin master
```
```git
git clone git@github.com:fagnerfgb/devops.git
```
```git
git checkout -b newbranch
git log
echo "Repositorio remoto" >> main.txt
git add .
git commit -m "alteracao no arquivo main.txt (teste remoto)"
git log
git push
git push --set-upstream origin newbranch
```
```git
git checkout master
cat main.txt
git pull
cat arquivo.txt
```
```git
git merge newbranch -m "fazendo merge da branch newbranch para a branch master"
git push
```
```git
echo "Nova linha no arquivo main" >> main.txt
git commit -am "Nova linha no main.txt"
git push
git pull
git config pull.rebase false
git log
git push
cat main.txt
cat arquivo.txt
```
```git
echo "Resolvendo conflitos - usuario local" >> fagner.txt
cat fagner.txt
git commit -am "alteracao local"
git pull
vim fagner.txt
git commit -am "conflito resolvido"
git push
```
```git
echo "nova linha local fetch" >> main.txt
git commit -am "nova alteracao"
git fetch origin
cat main.txt
git branch -r
git checkout origin/master
cat main.txt
git diff master origin/master
git checkout master
git merge origin/master
vim main.txt
git commit -am "Merge com git fetch"
git push
cat main.txt
```
```git
git log
git log arquivo.txt
git log --oneline
git log --stats
git log --stat
git log -p
git log -n 2
git log --graph
git log --graph --oneline
git log --author="Fagner Geraldes Braga"
git log --after="1 week ago"
```