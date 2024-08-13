num = int(input("Enter a number: "))
for i in range(num+1):
    isprime = True
    for n in range(2,i):
        if i%n == 0:
            isprime = False
if isprime:
    print("Prime number")
else:
    print("Not a prime number")
