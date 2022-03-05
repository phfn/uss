#!/bin/python3
from argparse import ArgumentParser
from os import system, makedirs

def parse_args():
    parser = ArgumentParser()
    # parser.add_argument("user", help="user to add")
    parser.add_argument("users", nargs="+", help="Users to add")
    return parser.parse_args()

def add_ssh_key(user):
    ssh_key = input("Please past the public ssh_key:\n")
    makedirs(f"/home/{user}/.ssh")
    with open(f"/home/{user}/.ssh/authorized_keys", "w+") as file:
        file.write("\n")
        file.write(ssh_key)

    pass


def add_user(user: str):
    groups = f"{user},docker,sudo"
    system(f"sudo useradd --create-home --groups {groups}")
    system(f"passwd {user}")
    add_ssh_key(user)


def main():
    args = parse_args()
    for user in args.users:
        add_user(user)


if __name__ == "__main__":
    main()
