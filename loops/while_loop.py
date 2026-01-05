#check prime or not
'''num=int(input('enter a n:'))
if num>2:
    i=2
    while i<=num//2:
        if num%i==0:
            print('not prime')
            break
        i=i+1
    else:
        print('prime')
else:
    print('not prime')'''

# Find the Nth prime number
# Input: N = 5
# Output: 11
'''n=int(input('n:'))
cnt=0
num=2
while True:
    for i in range(2,(num//2)+1):
        if num%i==0:
            break
    else:
        cnt+=1
        if cnt==n:
            print(num)
            break

    num+=1'''
# Print N number of prime numbers
# Input: N = 5
# Output: 2, 3, 5, 7, 11
n=int(input('n:'))
num=2
op=[]
while True:
    for i in range(2,(num//2)+1):
        if num%i==0:
            break
    else:
        op.append(num)
        if len(op)==n:
            print(op)
            break
    num+=1





