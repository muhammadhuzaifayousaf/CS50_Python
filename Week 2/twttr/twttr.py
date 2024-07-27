vowels = ['a', 'i', 'o', 'u', 'e']
str = input("Input: ")
print("Output: ", end='')


for text in str:
    if not text.lower() in vowels:
        print(text, end='')
print()
