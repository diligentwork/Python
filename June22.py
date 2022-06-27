'''
#doubt tried from online portal
while True:
     result = input("Enter 1-26:")
     if result.isdigit() and 1 <= int(result) <= 26:
         break;
     print ("Error Invalid Input")
'''
'''
#doubt tried from onlinr portal and need to check :

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
'''
'''
#program1
email = input("Enter your email id: ")

i = 0 
while i<len(email):
	print(email[i])
	i+=1
'''
'''
email = input("Enter your email id: ")

i = 0 
while i<len(email):
	if email[i]>='0' and email[i]<='9':
		print(email[i])
	i+=1 

'''
'''
#program2
email = input("Enter your email id: ")

i = 0 
while i<len(email):
	if email[i]>='a' and email[i]<='z':
		print(email[i],' ')
	i+=1 
'''
'''
#program3

email = input("Enter your email id: ")
i = 0 
while i<len(email): 
	if email[i]!='@':
		print(email[i])
	else:
		break
	i+=1 
'''

'''
#program4

email = input("Enter your email id: ")
i = 0 
while i<len(email): 
	if email[i]!='@':
		print(email[i], end='')
	else:
		break
	i+=1
'''
'''
#program5
email = input("Enter your email id: ")
i = 0 
while i<len(email): 
	if email[i]!='@':
		print(email[i], end='*')
	else:
		print()
		break
	i+=1 
'''
'''
#program6
email = input("Enter your email id: ")
i = 0 
while i<len(email): 
	if email[i]!='@':
		print(email[i], end='',sep='*')
	else:
		print()
		break
	i+=1 
'''
'''
#program7
email = input("Enter your email id: ")
i = 0 

while i<len(email): 
	if email[i]!='@':
		i+=1
		continue
	else:
		j = i+1
		while j<len(email):
			print(email[j], end = ' ')
			j+=1
		break
	i+=1 
'''
'''
#program8
email = input("Enter your email id: ")
i = 0 #preethi@gmail.com
index_of_at = email.index('@')
start = index_of_at+1
while start<len(email):
    print(email[start],end=' ')
    start+=1
'''
'''
#program9
email = input("Enter your email id: ")
i = 0 #preethi@gmail.com
index_of_at = email.index('*')
start = index_of_at+1
while start<len(email):
	print(email[start],end=' ')
	start+=1 
'''
#program10
#Type error
'''
no =1234
print(no[0])
'''
'''
number=1
f=1
while number<=10 :
    f=f*number
    number=number+1
print (f)
   
'''  


























