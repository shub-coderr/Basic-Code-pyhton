"""To count zero in given number
input = 1001 == output = No of zeros = 2 """
n=int(input("Enter the number"))
count=0
while(n!=0):
    d = n % 10
    if(d == 0):
        count=count+1

    n=n//10
print("No of zeros = ",count)