import csv
import sys


def main():
    if len(sys.argv) != 3:
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        with open(input_file, "r") as file:
            reader = csv.DictReader(file)
            rows = []

            for row in reader:
                last, first = row["name"].split(", ")
                house = row["house"]
                rows.append({"first": first, "last": last, "house": house})

    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")

    with open(output_file, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    main()
