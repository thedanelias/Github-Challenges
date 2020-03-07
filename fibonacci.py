#Program to find the fibonacci to the nth number

num = int(input("what nth term would you like the fibonacci series to?\n"))
fib1 = 0
fib2 = 1
fibresult = 0
fiblist = []
count = 1

while count <= num:
    fiblist.append(fibresult)
    fibresult = fib1 + fib2
    fib2 = fib1
    fib1 = fibresult
    count += 1

print(*fiblist, sep = ", ")