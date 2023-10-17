#№21-667
#Вариант 0
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

arr = [1, 2, 4, 6, 8, 10, 12]
target = 6
result = binary_search(arr, target)
if result != -1:
    print("Элемент найден в позиции", result)
else:
    print("Элемент не найден")