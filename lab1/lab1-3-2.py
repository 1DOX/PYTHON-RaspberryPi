def fibo(n):
    a = 1
    b = 2
 
    for i in range(n):
        yield a
        a, b = b, a + b

f = fibo(9)
for num in f:
    print(num)