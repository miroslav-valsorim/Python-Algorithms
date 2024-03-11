def merge_sort(array):
    if len(array) > 1:
        left = array[:len(array)//2]
        right = array[len(array)//2:]

        merge_sort(left)
        merge_sort(right)

        i = 0  # left
        r = 0  # right
        k = 0  # merged array index

        while i < len(left) and r < len(right):
            if left[i] < right[r]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[r]
                r += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while r < len(right):
            array[k] = right[r]
            r += 1
            k += 1

    return array


print(merge_sort([5, 4, 2, 7, 1, 8, 3]))
