def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            # print(f'Found in cache: {n}!')
            return cache[n]

        # print(f'Not found in cache. Calling "fibonacci" for {n}')
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

        return cache[n]

    return fibonacci

fib = caching_fibonacci()

print(fib(10))
print(fib(15))

