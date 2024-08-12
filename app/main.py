import sys


def main():

    command_set = set()
    # Uncomment this block to pass the first stage

    while(1):
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        command = input()

        print(f"{command}: command not found")


if __name__ == "__main__":
    main()
