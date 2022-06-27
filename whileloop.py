'''
Program1: Write a program in Python to display the Factorial of a number

n = int(input("Enter number: ")) # 5
if(n == 0 or n < 0):
    print("Value of n should be greater than 1")
else:
    fact = 1
    while(n):
        fact *= n
        n = n-1
    print(f"Factorial is {fact} ")

'''

#Program2: Write a program in Python to reverse a word.
'''
reverse_word="python"
len(reverse_word)
while i>=5:
    i=i+1
print (reverse_word[1])
    
'''
#formatted String:
# %i --> int
# %d --> int
# %f --> float
# %s --> string
'''
a,b,c = 100,200,300
name = "kavitha"
print("a value %d"%a)
print("name value %s"%name)
'''
# write a Program to type middle of the input name should be Uppercase.
name=input("Enter your name:")
print (len(name))
mid= len(name)/2
print(mid)

