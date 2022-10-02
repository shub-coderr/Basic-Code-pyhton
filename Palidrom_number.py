n = int(input("Enter the number\n"))
s=0
a=n
while(n!=0):
    d = n % 10
    s = s * 10 + d
    n = n // 10
if(a==s):
    print("Palidrome number")
else:
    print("Not Palidrome number")
