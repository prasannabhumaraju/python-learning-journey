#Password strength checker
#Write a program to check if a password is strong:
#At least 8 characters
#Contains digit and special character
'''pwd=input('p:')
spl="!@#$%^&*"

d=[]
sp=[]
for c in pwd:
    if c.isdigit():
        d.append(c)
    if c in spl:
        sp.append(c)
if len(pwd)>8 and len(d)>0 and len(sp)>0:
    print('strong pasword')
else:
    print('weak password')'''
#Validate email format
'''import re
gmail=input('mail:')
pattern=r'^[a-zA-Z0-9.-/%+_]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
if re.match(pattern,gmail):
    print('valid mail')
else:
    print('invalid mail')'''

#Salary tax calculation

#Salary ≤ 5L → No tax

#5L–10L → 10%

#10L → 20%
'''sal=int(input('sal:'))
if sal<=500000:
    tax=0
elif sal<1000000:
    tax=sal*0.10
else:
    tax=sal*0.20
print('tax:',tax)'''

#Find the middle number among three 
'''x=int(input())
y=int(input())
z=int(input())
if (x>y and x<z) or (x<y and x>z):
    print(x)
elif (y>z and y<x) or (y>x and y<z):
    print(y)
else:
    print(z)'''
#Check if characters are in increasing order
'''s=input()
if s[0]<s[1]<s[2]:
    print('increasing order')
else:
    print('not in order')'''

#Login with attempt limit
for atmpt in range(1,4):
    user=input('user:')
    pwd=input('pwd:')
    if user=='admin' and pwd=='2300':
        print('login sucessful')
    else:
        print(atmpt,'try again')
else:
    print('account locked')