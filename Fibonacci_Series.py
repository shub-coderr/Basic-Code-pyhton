"""
f1=0---------> Term1
f2=1--------->f1----->Term2
f2+f1=f3----->f2----->Term3
0+0=0
0+1=1
1+2=3
3+2=5
5+3=8
"""
n=int(input("Enter the number\n"))
t=3
f1 = 0
f2 = 1
print(f1)
print(f2)
for i in range(1, n-1):
 f3 = f2 + f1
 #print("f3", f3,"=","f1",f1,"f2",f2)
 print(f3)
 f1=f2
 f2=f3
 t=t+1

