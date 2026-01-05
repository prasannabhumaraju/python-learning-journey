'''n=5
for i in range(n):
    print('rama')'''
#check the given num is prime or not
'''n=int(input('enter a num:'))
if n>1:
    for i in range(2,(n//2)+1):
        if n%i==0:
            print('not prime')
            break
    else:
        print('prime')
else:
    print('not prime')'''
# Find all prime numbers in the given range
# Input: start = 10, end = 30
# Output: 11, 13, 17, 19, 23, 29
'''s=int(input('s:'))
e=int(input('e:'))

for num in range(s,e+1):
    if num>1:
        for i in range(2,(num//2)+1):
            if num%i==0:
                break
        else:
            print(num,end=" , ")'''
# Find the prime factors of the given number
# Input: N = 10
# Output: 2, 5
'''n=int(input('enter a num:'))
fac=[]
for i in range(2,(n//2)+1):
    if n%i==0:
        fac.append(i)
        n=n//i
print(fac,sep=",")'''

# Print alternative prime numbers in the given range
# Input: start = 2, end = 20
# Output: 2, 5, 11, 17
'''s=int(input('s:'))
e=int(input('e:'))
p=[]
for n in  range(s,e+1):
    if n>1:
        for i in range(2,(n//2)+1):
            if n%i==0:
                break
        else:
            p.append(n)
print(p[::2],sep=",")'''
# Print prime numbers up to N such that the reversed number is less than the original number
# Input: N = 35
# Output: 2, 3, 5, 7, 11, 13
n=int(input('n:'))
for num in range(2,n+1):
    for i in range(2,(num//2)+1):
        if num%i==0:
            break
    else:
        rev=0
        temp=num
        while temp>0:
            rev=rev*10+(temp%10)
            temp=temp//10
        if rev<=num:
            print(num,sep=",")




