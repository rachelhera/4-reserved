print("Enter name seperated by hypens: ")
name = input()
split = name.split("-")
for i in split:
    x = i[0]
    print(x, sep=' ')
