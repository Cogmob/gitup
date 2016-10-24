#!/bin/bash
echo 'initialising repo '$1
cd ~
rm -rf ~/$1
mkdir $1
cd $1
git clone git@bitbucket.org:Cogbot/node_base.git
rm -rf node_base/.git
cp -rT node_base .
rm -rf node_base
cat LICENCE.md | sed "s/yyyy/$(date '+%Y')/g" > LICENCE.md
git init
git add *
git commit -am 'set up project structure'
if [ $2 = "github" ]; then
    git remote add origin git@github.org:Cogmob/$1.git
else
    git remote add origin git@bitbucket.org:Cogbot/$1.git
fi
git push --force -u origin master
