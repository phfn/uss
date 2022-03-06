#!/bin/python3
from argparse import ArgumentParser
from os import system, makedirs, getuid
from getpass import getpass

def run(cmd: str):
    print(cmd)
    return system(cmd)

if getuid()!=0:
    print("Please use this script as root")
    exit(1)

parser = ArgumentParser()
parser.add_argument("users", nargs="+", help="Users to add")
args = parser.parse_args()

for user in args.users:
    print(f"Adding user {user}")
    groups = "docker,sudo"
    password = getpass("Please enter a password: ")
    ssh_key = input("Please past the public ssh_key:\n")

    run(f"useradd --create-home --groups {groups} --shell /bin/bash {user}")
    system(f"echo \"{user}:{password}\" | chpasswd")

    makedirs(f"/home/{user}/.ssh", exist_ok=True)
    with open(f"/home/{user}/.ssh/authorized_keys", "w+") as file:
        file.write("\n")
        file.write(ssh_key)
