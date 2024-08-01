import emoji

str = input("Input: ")
e = emoji.emojize(str, language='alias')
print("Output:", e)
