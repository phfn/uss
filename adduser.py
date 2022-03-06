#!/bin/python3
from argparse import ArgumentParser
from os import system, makedirs, getuid
from getpass import getpass
from subprocess import Popen
from crypt import crypt

def is_root():
    return getuid()==0

def parse_args():
    parser = ArgumentParser()
    parser.add_argument("users", nargs="+", help="Users to add")
    return parser.parse_args()

def add_ssh_key(user, ssh_key):
    makedirs(f"/home/{user}/.ssh", exist_ok=True)
    with open(f"/home/{user}/.ssh/authorized_keys", "w+") as file:
        file.write("\n")
        file.write(ssh_key)


def run(cmd: str, should_print = True):
    if print:
        print(cmd)
    return system(cmd)




def add_user(user: str):
    groups = "docker,sudo"
    password = getpass("Please enter a password: ")
    ssh_key = input("Please past the public ssh_key:\n")
    run(f"useradd --create-home --groups {groups} --shell /bin/bash {user}")
    run(f"echo \"{user}:{password}\" | chpasswd", should_print = False)
    add_ssh_key(user, ssh_key)


def main():
    args = parse_args()

    if not is_root():
        print("Please use this script as root")
        exit(1)

    for user in args.users:
        add_user(user)


if __name__ == "__main__":
    main()
