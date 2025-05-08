import os
import shutil
import subprocess
import sys


def main():
    while True:
        sys.stdout.write("$ ")

        # Wait for user input
        command = input()
        command_split = command.split(" ", 1)
        command_name, command_argument = (command_split[0], command_split[1]) if len(command_split) > 1 else (command, None)
        if command == "exit 0":
            break
        elif command_name == "echo":
            print(command_argument)
        elif command_name == "type":
            if command_argument in ["exit", "echo", "type", "pwd", "cd"]:
                print(f"{command_argument} is a shell builtin")
            elif path := shutil.which(command_argument):
                print(f"{command_argument} is {path}")
            else:
                print(f"{command_argument}: not found")
        elif command_name == "pwd":
            print(os.getcwd())
        elif command_name == "cd":
            if command_argument == "~":
                os.chdir(os.environ['HOME'])
            elif os.path.isdir(command_argument):
                os.chdir(command_argument)
            else:
                print(f"cd: {command_argument}: No such file or directory")
        elif shutil.which(command_name):
            subprocess.run(command.split())
        else:
            print(f"{command}: command not found")

if __name__ == "__main__":
    main()
