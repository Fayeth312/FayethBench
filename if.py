salary = int(input("What is your salary? "))
years = int(input("How many years have you worked here? "))

if years >= 5:
    print(f"Your bonus will be {salary * 0.05}")
else:
    print("You do not qualify for a bonus.")

Length = int(input("What is the length? "))
Width = int(input("What is the width? "))

if Length == Width:
    print(f"It's a square")
else:
    print("It's not a square.")

First = int(input("What is your first number? "))
Second = int(input("What is your second number? "))

if First > Second:
    print(f"The first number is larger")
if  First < Second:
    print(f"The second number is larger")
else:
    print("It's equal")

Classesheld = int(input("What is the number of classes held? "))
Classesattended = int(input("What is the number of classes you have attended? "))

if  Classesattended < 75:
    print(f"Your will not be allowed to sit in your exam")
else:
    print("Your will be allowed to sit in your exam")

first = int(input("What is the age of the first child? "))
second = int(input("What is the age of the second child? "))
third = int(input("What is the age of the third child? "))

if first > second and first > third:
    print(f"The first child is the oldest.")
elif second > third and second > first:
    print(f"The second child is the oldest")
elif third > second and third > first:
    print(f"The third child is the oldest")

if first < second and first < third:
    print(f"The first child is the youngest.")
elif second < third and second < first:
    print(f"The second child is the youngest")
elif third < second and third < first:
    print(f"The third child is the youngest")