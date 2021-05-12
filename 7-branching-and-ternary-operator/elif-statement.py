score = int(input("Enter number: "))

if 80 <= score <= 100:
    print("Final score is A")
elif 75 <= score < 80:
    print("Final score is B")
elif 70 <= score < 75:
    print("Final score is C")
elif 56 <= score < 70:
    print("Final score is D")
elif 0 <= score < 56:
    print("Final score is E")
else:
    print("Input score is not valid")
