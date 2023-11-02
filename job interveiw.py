name = input("Welcome. Before we we start this interveiw, what is your name? ")
start_interview = print(f"Alright {name}! Let's start.")
first = input("What type of job would you like? ")
second = int(input("How many years of experience do you have with this job? "))

if second < 5:
    print("I'm sorry. At this time we are looking for someone with more experience. Please apply again later.")
    exit()

sentance1 = print("Good to know. ")
third = int(input("What is your salary you would like you make? "))

if third > 50000:
    print("I'm sorry. We don't have that kind of money.")
    exit()

fourth = print (f"You said you would like to be a {first}. Why?")
user = input("" )
small_talk = print ("Alright, good to know.")
fifth = input("What are three of your greatest strengths? ")
sixth = int(input("How old are you? "))

if third < 14:
    print("I'm sorry, you need to be 14 or older. Try again when your old enough.")
    exit()

seventh = print(f"What are your goals by being a {first}? ")
user2 = input("" )
eighth = input("Is this your first job? ")
ninth = input("What motivates you? ")
tenth = input("Why should I hire you? " )