n = int(input("Enter the number\n"))
count=0

while(n!=0):
    n = n // 10
    count=count+1
    print("n= ",n)
    print("c= ",count)
print("Total number is: ",count)

