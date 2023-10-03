#1
w = 'PARADIGM'

for i in range(len(w)):
    print(w[i])
#2
for i in range (0, 5) :
    print (i)
#3
for i in range(1):
    print('Cat','Dog','Tiger','Cow')
print()
#4
for i in reversed(range (1, 11)) :
    print (i)
#5
flowers = ['Jasmine','Lotus','Rose','Sunflower']

for item in flowers:
    print(item)
else: 
    print ("Done")

#6
list1 = [5,10,15,20]
list2 = ['Tomatoes','Potatoes','Carrots','Cucumbers']
 
for i in list1:
   for j in list2:
      print(i,j)

#7 
numbers = [12,3,56,67,89,90]
sum = 0

for i in numbers: 
    sum += 1 

print (sum)

#8
vehicles = ['Car','Cycle','Bus','Tempo']

for i in vehicles:
    if i == "Bus":
        break
else:
    print(i)