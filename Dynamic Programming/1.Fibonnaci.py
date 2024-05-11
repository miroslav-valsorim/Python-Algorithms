# def calc_fib(n):
#     if n <= 2:
#         return 1
#
#     return calc_fib(n - 1) + calc_fib(n - 2)
#
#
# n = int(input())
#
# print(calc_fib(n))

# OPTIMIZED (with memorization)
def calc_fib(n, memory):
    if n in memory:
        return memory[n]

    if n <= 2:
        return 1

    result = calc_fib(n - 1, memory) + calc_fib(n - 2, memory)
    memory[n] = result
    return result


n = int(input())

print(calc_fib(n, {}))
