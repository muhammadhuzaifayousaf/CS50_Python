str = input("What is the answer to the Great Question of Life, the Universe and Everything? ").lower().strip()

if str == "42":
    print("Yes")
elif str == "forty-two":
    print("Yes")
elif str == "forty two":
    print("Yes")
else:
    print("No")
