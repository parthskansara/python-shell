import sys, os
import subprocess
import shlex

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

def search_executable(command):
    # Searches if args is a valid executable file

    # if command is an absolute path
    if os.path.exists(command):
        return command

    
    possible_paths = os.getenv('PATH').split(";")
    for path in possible_paths:
        file = f"{path}\\{command}"
        if os.path.exists(file):
            return file
    return False


def type_command(command, args, command_set):
    
    if args in command_set:
        print(f"{args} is a shell builtin")

    executable = search_executable(args)
    if executable: 
        print(f"{args} is {executable}")

    else:
        print(f"{args}: not found")

def run_program(command, args):
    try:
        user_input = [command, *args]
        if command.endswith('.py'):
            user_input.insert(0, "python")

        result = subprocess.run(user_input, capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Process failed with error code: {e.returncode}")



def main():
    command_set = set(["exit", "echo", "type"])
    exit_status = ""

    # Manually setting PATH variable for testing
    os.environ["PATH"] = "C:\\Users\\Parth\\Git\\codecrafters-shell-python;C:\\Users\\Parth\\Git\\codecrafters-shell-python\\app"
    

    run = True
    while(run):
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        user_input = shlex.split(input())


        command, args = user_input[0], user_input[1:]  
            

        if command not in command_set:
            executable = search_executable(command)
            if executable:
                run_program(command, args)
            else:
                invalid_command(command)
                continue

        if command == "exit":
            run = False
            exit(args, exit_status)

        elif command == "echo":
            echo(args)

        elif command == "type":
            type_command(command, args[0], command_set)



if __name__ == "__main__":
    main()
