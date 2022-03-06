#!/bin/bash
echo "Installing python..."
echo "sudo apt-get install python3.8 python-is-python3 python3-pip"
sudo apt-get install python3.8 python-is-python3 python3-pip
echo ""

echo "installing aws-shell"
pip install aws-shell
echo "pip install aws-shell"

echo "Installing docker"
./docker.sh
echo ""

echo "Adding user"
./adduser.py phillip juergen willi klaus sebastian
echo ""
