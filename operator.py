'''
#Program 1
mark = int(input("Please Enter Your Mark:"))
if mark>60:      
    print ("A Grade")
else:
    print("B Grade")
    
'''
'''
#Program 2
name = input("What is your Name:")
if name == "Diligent":
    print ("Welcome",name)
else:
    print("Welcome Guest!")
'''
'''
#Control Flow

mark = int(input("Enter Mark: "))
if mark>=90:
	print("A Grade")
elif mark>=70:
	print("B Grade")
elif mark>=60:
	print("C Grade")
else:
	print("Good ") 
'''
'''
#Program 3
import random

mind = random.randint(1,11)
guess = int(input("Enter any guess between 1 and 10 "))
while True: 
	if mind == guess:
		print("Yes, Your guess is correct")
		break
	else:
		guess = int(input("Enter any guess between 1 and 10 "))

'''
'''
#Program 4
import random

mind = random.randint(1,11)
guess = int(input("Enter any guess between 1 and 10 "))
while True: 
	if mind == guess:
		print("Yes, Your guess is correct")
		break
	else:
		guess = int(input("Enter any guess between 1 and 10 "))
'''
'''
#Program 5
end = int(input("Enter number "))
start = 1
while end>=1:
	print(start)
	end-=1 
'''
'''
end = int(input("Enter number "))
start = 1
while start<=end:
	print(start)
	start+=1 

'''
'''
#Program 6
end = int(input("Please Enter The Number:"))
first = 1
while first <= end:
    if first%2==0:
        print(first)
    first+=1

'''

'''
#Program 7
end = int(input("Enter number "))
first = 1
while first<=end:
	if first%3==0 and first%2==0:
		print(first)
	first+=1 
'''
'''
#Program 8
end = int(input("Enter number "))
first = 1
while first<=end:
	if first%3==0 or first%2==0:
		print(first)
	first+=1 
'''
'''
#Program 9
end = int(input("Enter number "))
first = 1
while first<=end:
	print(first)
	if first==5:
		break
	first+=1 

'''
'''
#Program 10
end = int(input("Enter number "))
first = 1
while first<=end:
	if first==5:
		first+=1
		continue
	print(first)
	first+=1 
'''






