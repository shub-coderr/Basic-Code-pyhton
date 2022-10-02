"""To check number has zero or not
input = 1045 == output = Yes it has zero as digit"""
n=int(input("Enter the number"))
a=n
flag=0
while(n!=0):
    d = n % 10
    if(d == 0):
        flag=1
        break
    n = n//10
if flag==1:
    print("Yes it has zero as digit")