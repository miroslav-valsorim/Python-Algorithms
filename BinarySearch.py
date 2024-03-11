# def binary_search(array, item):
#     begin_index = 0
#     end_index = len(array) - 1
#
#     while begin_index <= end_index:
#         midpoint = begin_index + (end_index - begin_index) // 2
#         midpoint_value = array[midpoint]
#         if midpoint_value == item:
#             return midpoint
#         elif item < midpoint_value:
#             end_index = midpoint - 1
#         else:
#             begin_index = midpoint + 1
#     return None
#
#
# array_a = [2, 4, 7, 10, 13, 3]
# item_a = 4
# print(binary_search(array_a, item_a))

# 2nd
# def binarySearch(array, x, low, high):
# #     if high >= low:
# #         mid = low + (high - low)//2
# #         # If found at mid, then return it
# #         if array[mid] == x:
# #             return mid
# #         # Search the left half
# #         elif array[mid] > x:
# #             return binarySearch(array, x, low, mid-1)
# #         # Search the right half
# #         else:
# #             return binarySearch(array, x, mid + 1, high)
# #     else:
# #         return -1
# #
# #
# # array = [3, 4, 5, 6, 7, 8, 9]
# # x = 9
# #
# # result = binarySearch(array, x, 0, len(array)-1)
# #
# # if result != -1:
# #     print("Element is present at index " + str(result))
# # else:
# #     print("Not found")


# 3rd
def binary_search(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid_index = (left + right) // 2
        mid_elem = array[mid_index]
        if mid_elem == target:
            return mid_index

        if mid_elem < target:
            left = mid_index + 1
        elif mid_elem > target:
            right = mid_index - 1

    return f"the number is not in this array"


numbers_we_have = [1, 2, 3, 4, 5, 6, 7]
number_we_search = 7
print(binary_search(numbers_we_have, number_we_search))

