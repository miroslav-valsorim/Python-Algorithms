def factorial(n):
    if n <= 1:
        return n
    else:
        return n * factorial(n - 1)


num = int(input())
print(factorial(num))
# print(factorial(5))  # 120
