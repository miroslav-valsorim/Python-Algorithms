def reverse_array(array):
    if len(array) <= 1:
        return array
    else:
        return [array[-1]] + reverse_array(array[:-1])


print(reverse_array([5, 4, 3, 2, 1]))  # [1, 2, 3, 4, 5]
