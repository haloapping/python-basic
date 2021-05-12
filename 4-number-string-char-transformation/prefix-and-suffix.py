# rstrip (prefix)
print("Rahel cantik      ")
print("Rahel cantik      ".rstrip())

print()

# lstrip (suffix)
print("       Rahel cantik")
print("       Rahel cantik\n".lstrip())

# strip (prefix and suffix)
print("       Rahel cantik      ")
print("       Rahel cantik      ".strip())

# Select character you want to delete
word = "rahelcuek"
print("Strip:", word.strip("ek"))

# startswith() mengecek apakah awal kata pada kalimat ada sesuai dengan yang dicari
print("Apping Rahel".startswith("Apping"))

# endswith
print("Apping Rahel".endswith("Rahel"))

# Separate and combine string
# join()
print(" ".join(["Apping", "Sayang", "Rahel"]))

# split()
print("Apping sayang rahel".split())

# Replace string
title = "Cintaku berujung kesedihan"
print(title.replace("kesedihan", "kebahagiaan"))

title_1 = "cinta ku dan cinta dia berujung kesedihan"
print(title_1.replace("cinta", "bahagia", 1))
print(title_1.replace("cinta", "bahagia", 2))

# String check
# isupper()
print("RAHEL".isupper())

# islower()
print("rahel".islower())

# isalpha()
print("rahel".isalpha())

# isalnum()
print("Rahel1998".isalnum())

# isdecimal()
print("12993".isdecimal())

# isspace()
print(" ".isspace())

# istitle
print("Saya Suka Makan Martabak Manis".istitle())

# while True:
#     name = input("Enter your name: ")
#
#     if name.isalpha():
#         print("Halo", name)
#         break
#
#     print("Enter your correct name.")

# Formatting in string
number = 5
print(str(number).zfill(5))

number = 300
print(str(number).zfill(5))

number = -0.45
print(str(number).zfill(5))

number = -0.45
print(str(number).zfill(7))

string = "Apping"
print(string.zfill(10))

# Text position right, left, center
# rjust()
print("Apping".rjust(20))

# ljust()
print("Rahel".ljust(20, ":"))

# center
print("Apping".center(20, "-"))

# String literals
print("Jum'at\nyuk")

# Raw string
print(r"Kapan yah bisa ketemu sama kamu:\tSemoga secepatnya yah")






