import sys

def invalid_command(command):
    print(f"{command}: command not found")

def exit(args, exit_status):    
    if args:
        exit_status = args[0]
    print(f"exit status: {exit_status}")

def echo(args):
    for arg in args:
        print(f"{arg}", end= " ")
    print("\b")

def type_command(command, args, command_set):
    args = " ".join(args)
    if args in command_set:
        print(f"{args} is a shell builtin")

    else:
        print(f"{args}: not found")



def main():
    command_set = set(["exit", "echo", "type"])
    exit_status = ""
    # Uncomment this block to pass the first stage
    run = True
    while(run):
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        user_input = input()
        command, args = user_input.split(" ")[0], user_input.split(" ")[1:]

        if command not in command_set:
            invalid_command(command)
            continue

        if command == "exit":
            run = False
            exit(args, exit_status)

        elif command == "echo":
            echo(args)

        elif command == "type":
            type_command(command, args, command_set)



if __name__ == "__main__":
    main()
