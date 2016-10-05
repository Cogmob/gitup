#!/bin/bash
echo 'initialising repo '$1
cd ~
cd $1
echo 'asdf' >> README.md
echo 'gen' >> .gitignore
mkdir src
mkdir gen
