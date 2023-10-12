num = int(input("What is the number of numbers you would like in your sequence?: "))

x = 0 
y = 1
z = y 
count =1

while count <= num:
    print(f"{z} ")
    count += 1
    x, y = y,z 
    z = x + y