def fib(n, memo={}) -> int:
    """
    Return value of n-th Fibonacci number.
    - input: n=8
    - output: 21
    """
    # your code

    # if _n == 0:
    #     return 0
    # if _n == 1:
    #     return 1
    # return self.fib(_n-1) + self.fib(_n-2)

    memo = {0: 0, 1: 1}
    i = 2
    if n < len(memo):
        return memo[n]
    else:
        while i < n:
            for i in range(i, n+1):
                fibnumber = (memo[i - 1]) + (memo[i - 2])
                memo.update({i: fibnumber})
                i = i+1
            break
        return memo[n]


print(fib(30))
print(fib(60))
