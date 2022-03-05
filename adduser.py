#!/bin/python3
from argparse import ArgumentParser
from os import system, makedirs
from getpass import getpass
from subprocess import Popen

def parse_args():
    parser = ArgumentParser()
    # parser.add_argument("user", help="user to add")
    parser.add_argument("users", nargs="+", help="Users to add")
    return parser.parse_args()

def add_ssh_key(user, ssh_key):
    makedirs(f"/home/{user}/.ssh", exist_ok=True)
    with open(f"/home/{user}/.ssh/authorized_keys", "w+") as file:
        file.write("\n")
        file.write(ssh_key)

    pass


def run(cmd: str, stdin = None):
    print(cmd)
    if not stdin:
        return system(f"echo \"{stdin}\" | {cmd}")
    return system(cmd)

def change_password(user, password):
    proc = Popen("chpasswd user")
    proc.stdin.write("pass")



def add_user(user: str):
    groups = "docker,sudo"
    password = getpass("Please enter a password: ")
    ssh_key = input("Please past the public ssh_key:\n")
    run(f"sudo useradd --create-home --groups {groups}")
    run("passwd", stdin=f"{password}\n{password}")
    add_ssh_key(user, ssh_key)


def main():
    args = parse_args()
    for user in args.users:
        add_user(user)


if __name__ == "__main__":
    main()
