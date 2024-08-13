a,b,c=map(int,input().split(","))
if(a>b and a>c):
    print("a is biggest number")
elif(b>c and b>a):
    print("b is biggest number")
else:
    print("c is biggest number")
