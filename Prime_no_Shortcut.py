n=int(input("Enter the number"))
for i in range(2,n//2+1):
    if n % i == 0:
       print("Not prime number")
       break
else:
    print("Prime number")