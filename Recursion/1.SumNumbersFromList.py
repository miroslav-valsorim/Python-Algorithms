def array_sum(nums, idx):
    if idx == len(nums) - 1:
        return nums[idx]
    else:
        return nums[idx] + array_sum(nums, idx + 1)


numbers = [int(x) for x in input().split()]

print(array_sum(numbers, 0))  # [1,2,3,4,5] = 15
