fib_cache = {} # Memoization cache

def fibonacci(n):
    if n in fib_cache:
        # If n is already in the cache, return the cached value
        return fib_cache[n]
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Compute the value for n and store it in the cache
        fib_cache[n] = fibonacci(n-1) + fibonacci(n-2)
        return fib_cache[n]


print(fibonacci(100))
