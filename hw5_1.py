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

    while True:
        user_input = input("Enter a number: ")

        if user_input in ["close", "exit"]:
            print("Good bye!")
            break
        else:
            print('-cache before-', cache)
            result = fibonacci(int(user_input))
            print('-cache AFTER-', cache)
            print(f'The number "{user_input}" from Fibonacci row is "{result}"')

caching_fibonacci()



