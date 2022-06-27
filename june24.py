#program 1 for GCD

'''
no1 = 100
no2 = 75
small = no1 if no1<no2 else no2
gcd = -1
div = 2
while div<=small:
    if no1%div==0 and no2%div==0:
        gcd = div
        print(div)
    div+=1
else:
    print("GCD is",gcd)

''' 
#program 2 for LCM
# while loop based on condition.
# while True is infinitie loop.

'''
no1=int(input("Please Enter the 1st Number:"))
no2=int(input("Please Enter the 2nd Number:"))
big=no1 if no1>no2 else no2
while True:
    if big%no1==0 and big%no2==0:
       print("LCM is ",big)
       break
    big+=1
'''

#Program 3 sum of digits
'''
box=int(input("Please Enter the 1st Number:"))
total=0
while box>0:
    rem=box%10
    print(rem)
    total=total+rem
    box=box//10
else:
    print(total)
'''

#Program 4 sum of digits

'''
box=int(input("Please Enter the 1st Number:"))
total=0
while box>0:
    rem=box%5
    print(rem)
    total=total+rem
    box=box//5
else:
    print(total)
'''
