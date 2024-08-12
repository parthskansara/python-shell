import sys


def main():

    command_set = set()
    exit_status = ""
    # Uncomment this block to pass the first stage
    run = True
    while(run):
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        user_input = input()
        command, args = user_input.split(" ")[0], user_input.split(" ")[1:]

        if command == "exit":
            run = False
            exit_status = args[0]
            print(f"exit_status: {exit_status}")
        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
