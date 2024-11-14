file = open("1984.txt", "r")


while True:
    text = file.read(1)
    text.lower()
    if (text.isalpha()):
        print(text)
    else:
        continue