def BubbleSort(array):
    # -1 because we cant iterate trough last index
    index_length = len(array) - 1
    sorted = False

    while not sorted:
        sorted = True

        for index in range(0, index_length):
            if array[index] > array[index + 1]:
                sorted = False
                array[index], array[index + 1] = array[index + 1], array[index]
                #print(array)

    return array


print(BubbleSort([4, 3, 2, 1, 6, 5, 8, 9, 7]))


# 2nd
# def bubble_sort_two(array):
#     for i in range(len(array)):
#         for j in range(1, len(array)-1):
#             if array[j-1] > array[j]:
#                 array[j], array[j-1] = array[j-1], array[j]
#     return array
#
#
# print(bubble_sort_two([4, 3, 2, 1, 6, 5, 8, 9, 7]))
#

