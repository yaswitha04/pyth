n=int(input("Enter a number :"))
fact=1
if n<0:
	print("Negative Number")
elif n==0:
	print("0 is 1")
else:
	for i in range(1,n+1):
		fact=fact*i
print("Factorial of",n,"is",fact)
