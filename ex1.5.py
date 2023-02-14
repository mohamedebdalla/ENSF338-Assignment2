import timeit
import matplotlib.pyplot as plt


# Original code:

def fib_original(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_original(n-1) + fib_original(n-2)

# Modified code:

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

x = range(36)
y_original = [timeit.timeit(lambda: fib_original(i), number=1) for i in x]
y_optimized = [timeit.timeit(lambda: fibonacci(i), number=1) for i in x]

plt.plot(x, y_original, label='Original code')
plt.plot(x, y_optimized, label='Optimized code')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('Fibonacci computation time')
plt.legend()
plt.show()


