def fac(n):
    if n == 0 or n == 1:
        return 1
    return n*fac(n-1)


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)


# print(fac(1))
# print(fac(2))
# print(fac(3))
print(fac(60))


for i in range(0, 60):
    print(i, fib(i))
# print(fib(40))
