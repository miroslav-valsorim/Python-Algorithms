def insertionSort(array):
    index_length = range(1, len(array))

    for i in index_length:
        value_to_sort = array[i]

        while array[i-1] > value_to_sort and i > 0:
            array[i], array[i-1] = array[i-1], array[i]
            print(i)
            i = i - 1

    return array
#
#
# print(insertionSort([4, 3, 2, 1, 6, 5, 9, 7, 8, 10]))

# 2nd
def insertion_sort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
            else:
                break
    return array


numbers_list = [4, 3, 2, 5, 1]
print(insertion_sort(numbers_list))
