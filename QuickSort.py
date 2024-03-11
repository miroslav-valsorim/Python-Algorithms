def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array.pop()

    items_greater = []
    items_lower = []
    for item in array:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


print(quick_sort([5, 4, 2, 7, 1, 8, 3]))
