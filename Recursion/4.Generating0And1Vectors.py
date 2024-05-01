def generate(idx, vector):
    if idx >= len(vector):
        print(*vector, sep='')
        return
    else:
        for num in range(2):
            vector[idx] = num
            generate(idx + 1, vector)


n = int(input())
vector = [0] * n

generate(0, vector)


# n = 3

# 0 0 0
# 0 0 1
# 0 1 0
# 0 1 1
# 1 0 0
# 1 0 1
# 1 1 0
# 1 1 1
