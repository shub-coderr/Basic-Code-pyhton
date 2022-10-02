"""To check if all digits of number divide it
input = 128:    128%1==0   128%2==0   128%8==0 ----> True"""
n=int(input("Enter the number"))
a=n
flag=0
while(n!=0):
    d = n % 10
    if d == 0 or a % d != 0:
        flag=1
        break
    n = n//10
if flag==0:
    print("Yes it is divided by all digits")
else:
    print("No")