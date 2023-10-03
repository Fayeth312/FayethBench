car_color = "Blue"
car_make = "Tesla"

if car_color == "Blue":
    if car_make == "Tesla":
        print("My car is a Blue Tesla")
    else:
        print("My car is blue")
elif car_color == "Red":
    print("My car is a ferrari")
else:
    print("I just have a bike")

#for loop
for i in range(1, 10):
    print(i)

sports = ['soccer', 'basketball', 'hockey', 'football']

for item in sports:
    print(item)

# #while loop
i = 1
while i < 6:
    print("I'm still going")
    i += 1

#break normally used in while loop, but can be used in for loops. its a way to end the loop if it hits a certan condition/number
for i in range(50):
    if i >24:
        break
    else:
        print(i)  