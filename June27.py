'''
#reverse number print
box1 = 1234
total = 0
while box1>0:
	rem = box1%10
	print(rem) #4 3 2 1
	total= (total*10)+rem
	box1 = box1//10 #123
else:
	print(total)

'''
'''

box1 = 1234
total = 0
while box1>0:
	rem = box1%10
	print(rem) #4 3 2 1
	total= (total*10)+rem
	box1 = box1//10 #123
else:
	print(total)


'''
'''
#error out not palindrome
box1 = 12321
reverse = 0
while box1>0:
	rem = box1%10
	print(rem) #4 3 2 1
	reverse= (reverse*10)+rem
	box1 = box1//10 #123
else:
	print(box1)
	print(reverse)
	if box1==reverse:
		print("Palindrome")
	else:
		print("Not Palindrome")

'''

'''


box1 = 12321
box2 = box1
reverse = 0
while box1>0:
	rem = box1%10
	print(rem) #4 3 2 1
	reverse= (reverse*10)+rem
	box1 = box1//10 #123
else:
	if box2==reverse:
		print("Palindrome")
	else:
		print("Not Palindrome")
'''

'''
#Decimal to binary
no = 1000
binary = ''
while no>0:
	val = no%2
	binary = str(val) + binary
	no = no//2
else:
	print(binary)

'''
'''
import math
no =110
i = 0
while no >0:
    rem=no%10
    val=rem*(int(math.pow(2,i))
    decimal=decimal+value
    no=no//10
'''
'''
import math
no = 1010
decimal = 0
i = 0 
while no>0:
	rem = no%10
	val = rem * (int(math.pow(2,i)))
	decimal = decimal +  val
	no = no//10
	i+=1
else:
	print(decimal) 

'''
'''
import math

print(math.pow(2,2))

print(math.pow(3,5))
print(type(math.pow(3,5)))

'''
'''
#task :
1) Armstrong Number
2) Neon number
3) Strong Number
4) Perfect Nu

'''
