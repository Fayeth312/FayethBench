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
    print("I'm sorry. We don't have that amout of money to give.")
    exit()

fourth = input(f"You said you would like to be {first}. Why?")
small_talk = print ("Alright, good to know.")
fifth = input("What are three of your greatest strengths? ")
sixth = int(input("How old are you? "))

if third < 14:
    print("I'm sorry, you need to be 14 or older. Try again when your old enough.")
    exit()

seventh = input(f"What are your goals by being {first}? ")
eighth = input("Is this your first job? ")
ninth = input("What motivates you? ")
tenth = input("Why should I hire you? " )
recap = input(f"Alright {name}, congratualations on making it through the interveiw. I would like to reacap what we have gone over. You would like to be a {first}, you have {second} years of experience, you want your salary to be {third}, you want this job because {fourth}, your greatest strengths are {fifth}, you are {sixth} years old, your goals with being a {first} are {seventh}, was this your first job? {eighth}, {ninth} motivates you, and I should hire you because {tenth}. Is this right? Yes or No: ")

if recap == "yes" or "Yes": 
    print ("Alright. You are hired.")
else:
    print ("Alright. I'll look through my notes. I will contact you later.")