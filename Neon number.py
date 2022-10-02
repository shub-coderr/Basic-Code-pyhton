n = int(input("Enter the number\n"))
t=9**2
s=0
while(t!=0):
    d = t % 10
    s = s + d
    t = t // 10
if(n==s):
    print("Neon number")
else:
    print("Not Neon number")
