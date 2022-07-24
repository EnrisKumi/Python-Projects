number = int(input("Enter a number"))
nr1 = 1
nr2 = 1

fib = []

for i in range(20):
    nr1,nr2 = nr2, nr1+nr2
    fib.append(nr2)

print(fib)