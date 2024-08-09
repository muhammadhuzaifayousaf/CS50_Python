import sys

count = 0

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few commad-line arguements")
elif not sys.argv[1].endswith('.py'):
    sys.exit("Not python file")
else:
    try:
        with open(sys.argv[1], "r") as file:
            for line in file:
                stripped_line = line.strip()
                if stripped_line and not stripped_line.startswith('#'):
                    count += 1

        print(count)

    except FileNotFoundError:
        sys.exit("File does not exist!")
