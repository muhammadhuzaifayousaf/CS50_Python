import csv
import sys

from tabulate import tabulate

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few commad-line arguements")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")
else:
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            header = reader.fieldnames
            rows = [list(row.values()) for row in reader]
            print(tabulate(rows, header, tablefmt='grid'))

    except FileNotFoundError:
        sys.exit("File does not exist")
