alphabets = "ABCDEFGHIJKLMN"

for alphabet in alphabets:
    if alphabet == "F":
        break

    print("Current alphabet", alphabet)

print()

for i in range(0, 10):
    for j in range(0, 10):
        if j > i:
            print()
            break
        else:
            print("*", end="")
