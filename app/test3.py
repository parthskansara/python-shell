import sys

try:
    print(f"Arguments: {sys.argv[1:]}")
    print(f"Number of arguments: {len(sys.argv) - 1}")
    
    if len(sys.argv) < 2:
        print("No arguments provided", file=sys.stderr)
        sys.exit(1)
    
    sys.exit(0)  # Exit successfully
except Exception as e:
    print(f"An error occurred: {str(e)}", file=sys.stderr)
    sys.exit(2)