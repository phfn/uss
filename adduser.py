#!/bin/python3
from argparse import ArgumentParser
# from subprocess import run
from os import system

def run(args):
    for arg in args:
        print(arg, end=" ")
    print()

def parse_args():
    parser = ArgumentParser()
    # parser.add_argument("user", help="user to add")
    parser.add_argument("users", nargs="+", help="Users to add")
    return parser.parse_args()

def add_ssh_key(user):
    ssh_key = input("Please past the public ssh_key:\n")
    with open(f"/home/{user}/.ssh/authorized_hosts", "a") as file:
        file.write("\n")
        file.write(ssh_key)

    pass


def add_user(user: str):
    groups = ["docker"]
    groups_str = "user"
    for group in groups:
        groups_str += "," + group

    run(f"sudo useradd --create-home --groups {groups_str}".split(" ")  )
    run(f"passwd {user}".split(" "))
    add_ssh_key(user)


def main():
    args = parse_args()
    for user in args.users:
        add_user(user)


if __name__ == "__main__":
    main()
