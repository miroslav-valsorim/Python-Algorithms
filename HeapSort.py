def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def siftDown(array, i, upper):
    while True:
        l, r = i*2+1, i*2+2
        if max(l, r) < upper:
            if array[i] >= max(array[l], array[r]):
                break
            elif array[l] > array[r]:
                swap(array, i, l)
                i = l
            else:
                swap(array, i, r)
                i = r
        elif l < upper:
            if array[l] > array[i]:
                swap(array, i, l)
                i = l
            else:
                break
        elif r < upper:
            if array[l] > array[i]:
                swap(array, i, r)
                i = r
            else:
                break
        else:
            break


def heapsort(array):
    for j in range(len(array) - 2 // 2, -1, -1):
        siftDown(array, j, len(array))

    for end in range(len(array) - 1, 0, -1):
        swap(array, 0, end)
        siftDown(array, 0, end)

        
lst = [5, 16, 8, 4, 3]
heapsort(lst)
print(lst)
