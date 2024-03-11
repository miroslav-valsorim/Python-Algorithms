def selection_sort(array):
    index_length = range(0, len(array)-1)

    for i in index_length:
        min_value = i

        # finds the lowest number in the current iteration
        for j in range(i+1, len(array)):
            if array[j] < array[min_value]:
                min_value = j

        if min_value != i:
            array[min_value], array[i] = array[i], array[min_value]

    return array

# 2nd way
# def selection_sort(array):
#     sorted_list = []
#     while array:
#         min_number = min(array)
#         sorted_list.append(min_number)
#         array.remove(min_number)
#
#     return sorted_list

print(selection_sort([5, 4, 2, 7, 1, 8, 3]))
print(selection_sort([2, 5, 3, 1, 7, 0, 2, 4]))
print(*(selection_sort([2, 5, 3, 1, 7, 0, 2, 4])), sep=' ')