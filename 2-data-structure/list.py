# List dengan value bertipe data yang sama
lists_1 = [1, 2, 3, 4, 5]

# List dengan value bertipe data yang berbeda
lists_2 = ['1', 2, 3, True, 2.33, 4j]

print(lists_1[0])
print(lists_1[4])
print(lists_1[-1])  # ambil nilai terakhir dari list
print(lists_1[1:3])
print(lists_1[:5])
print(lists_1[-3])  # ambil nilai index paling belakang sejauh 3 dan seterusnya
print(lists_1[1:7:2])  # ambil nilai list dari index 1-6 dengan step 2

# Replace value with index list
print(lists_1[-1])
lists_1[-1] = 55
print(lists_1[-1])

# Add new value in list
print(lists_1)
lists_1.append(100)
print(lists_1)

# Delete value by index
del lists_1[-1]
print(lists_1)

# String slicing
word = "Cantik banget :)"
print(word[-1])
print(word[0:-1])

# word[1] = "))"
# print(word) # Gagal, karena string imutable
word = "Hi"
print(word)
