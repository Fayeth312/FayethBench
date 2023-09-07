my_name = "Fayeth" #global variable, accses able to the whole file

def give_a_name():
    a_name = "William"
    print(a_name)   #local variable, only accsessable to the function

print(my_name)

user_input = input("What is your name? ") #input= wait for response but put a space between parentheses and last word/charecter
print(f"Nice to meet you, {user_input}!") #output = is scripted

#data types
my_string = "This is my string." #ALWAYS wrapped in quotation marks
my_integer = 1456 #any whole number (positive or negitive)
my_float = 5.7 #any number that isn't a whole number, just a decimal even if it's 3.0 its still conciderd a float cause it has a decimal
is_my_boolean = True #True or False. HAS to be capitalized

print( my_integer + my_float)
print( my_float + my_float)

my_deeclaration = "" 
my_initialization = "hello world" 

#arithmatic operators 
add = 1+2 #(addition)
subtract = 2-1 #(subtraction)
divide = 2/1 #(division)
multiply = 1 * 3 #(multiplication)
modulo = 10 % 3 #(find remainder) 
exponent = 2 ** 3 #(exponent)
#mostly use top 5
print(modulo)

#comparison operators
statment = 4 > 2
statment2 = 4 >= 2
statment3 = 4 <= 2
statment4 = 4 == 2 #compare is it the same
statment5 = 4 != 2 #does not equal "the bang" operator

print(statment)
print(statment2)
print(statment3)
print(statment4)
print(statment5)

#message operators
message = 4 > 2 and 33 < 43
message2 = 4 < 2 or 33 < 43
x = False

print(message)
print(message2)
print(not x) #way to get opposite of something