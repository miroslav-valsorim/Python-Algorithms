def recursive_fibonnaci(n):
    if n <= 1:
        return n
    else:
        return recursive_fibonnaci(n - 1) + recursive_fibonnaci(n - 2)


def iterative_fibonacci(n):
    fib0 = 1
    fib1 = 1
    result = 0
    for _ in range(n - 1):
        result = fib0 + fib1
        fib0, fib1 = fib1, result

    return result


n = int(input())
print(iterative_fibonacci(n))
