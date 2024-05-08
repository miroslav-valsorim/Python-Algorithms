# def reverse_array(array):
#     if len(array) <= 1:
#         return array
#     else:
#         return [array[-1]] + reverse_array(array[:-1])
#
#
# print(reverse_array([5, 4, 3, 2, 1]))  # [1, 2, 3, 4, 5]

def reverse_array(idx, elements):
    if idx == len(elements) // 2:
        return

    swap_idx = len(elements) - 1 - idx
    elements[idx], elements[swap_idx] = elements[swap_idx], elements[idx]
    reverse_array(idx + 1, elements)


elements = input().split()

reverse_array(0, elements)
print(' '.join(elements))
