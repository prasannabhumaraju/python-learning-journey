#Write a program to check whether a number is positive, negative, or zero.
'''n=int(input("enter a num:"))
if n==0:
    print('zero')
elif n<0:
    print('negative')
else:
    print('positive')   '''

#Check if a number is even or odd
'''n=int(input('n:'))
if n%2==0:
    print('even')
else:
    print('odd')'''

#Find the largest of two numbers
'''n1=int(input('n1:'))
n2=int(input('n2:'))
if n1>n2:
    print(n1,'is largest')
else:
    print(n2,'is the largest')'''

#Check if a person is eligible to vote (age ≥ 18)
'''n=int(input('n:'))
if n>=18:
    print('you are eligible to vote')
else:
    print('not eligible')'''


#Find the largest of three numbers
'''n1=int(input('n1:'))
n2=int(input('n2:'))
n3=int(input('n3:'))
if n1>=n2 and n1>=n3:
    print(n1,'is largest')
elif n2>=n1 and n2>=n3:
    print(n2,'is the largest')
else:
    print(n3,'is the largest')'''

#Check if a year is a leap year
'''y=int(input('y:'))
if (y%4==0 and y%100!=0) or y%400==0:
    print('leap year')
else:
    print('not a leap year')'''

#Check if a character is a vowel or consonant
'''ch=input('ch:').lower()
if ch in 'a,e,i,o,u':
    print('vowel')
else:
    print('consonant')'''

#Grade system based on marks
'''m=int(input('marks:'))
if m>=90:
    print('got A grade,PASS')
elif m>=75:
    print('got B grade,PASS')
elif m>=60:
    print('got C grade,PASS')
else:
    print('FAIL')'''

#Check if a number is divisible by both 3 and 5
'''n=int(input('n:'))
if n%3==0 and n%5==0:
    print('divisible')
else:
    print('not divisible')'''

#Check if a triangle is valid using sides
'''x=int(input('x:'))
y=int(input('y:'))
z=int(input('z:'))
if x+y>z and y+z>x and z+x>y:
    print('triangle')
else:
    print('not triangle')'''

#Electricity bill calculation
'''u=int(input('u:'))
if u<=100:
    bill=u*1
elif u<=200:
    bill= 100*1+(u-100)*2
else:
    bill=100*1+100*2+(u-200)*3
print('bill:',bill)'''

#Login system using if–else
'''user=input()
pwd=input()
if user=='admin' and pwd=='psn@23':
    print('login sucess')
else:
    print('INVALID!')'''

#Check if a number is in a given range (10 to 50)
'''n=int(input('n:'))
if 10<=n<=50:
    print('in range')
else:
    print('out of range')'''

#ATM Withdrawal Validation
bln=10000
amt=int(input('amt'))
if amt<=bln and amt>0:
    print(amt,'is withdrawn sucessful')
    r=bln-amt
    print(r,'is remaining balance')
else:
    print('unsufficient balanace or invalid amt')
