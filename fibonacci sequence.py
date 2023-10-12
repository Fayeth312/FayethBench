def fibonacci():
    num = int(input("What is the number of numbers you would like in your sequence?: "))
    i = 1
    if num == 0:
        fib = []
    elif num == 1:
        fib = [1]
    elif num == 2:
        fib = [1,1]
    elif num > 2:
        fib = [1,1]
        while i < (num - 1):
            fib.append(fib[i] + fib[i-1])
            i += 1
    return fib
print (fibonacci())


# how_deep = int(input("Good day. How many numbers would you like your personalised fibonacci sequence?: "))

# def fibonacci(num):
#     for i in range(num):
#         x = i 
#         y = x
#         z = x + y
#         x = z 
#         print(x)
# fibonacci(how_deep)