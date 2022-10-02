n = int(input("Enter the number\n"))
x = a = n
s = count = 0
while(n != 0):
 count = count+1
 n = n // 10

while(a != 0):
    d = a % 10
    s = s + pow(d,count)
    a = a // 10
if(x == s):
    print("Armstrong number")
else:
    print("Not Armstrong number")
