import sys


def main():

    command_set = set()
    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Wait for user input
    command = input()

    if command not in command_set:
        sys.stdout.write(command + ": command not found")


if __name__ == "__main__":
    main()
