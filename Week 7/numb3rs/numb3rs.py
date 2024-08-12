import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = r"^(\d{1,3}\.){3}\d{1,3}$"

    if re.match(pattern, ip):
        addresses = ip.split(".")
        for address in addresses:
            if int(address) < 0 or int(address) > 255:
                return False
        return True
    return False


if __name__ == "__main__":
    main()
