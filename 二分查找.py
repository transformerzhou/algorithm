#二分查找，找到则返回下标，否则-1
def binarySearch(arr, left, right, x):
    while (left <= right):
        # 取中值
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid+1
        else:
            right = mid-1
    return -1

arr = [1,3,4,5,6,8,9]
x = 7
print(binarySearch(arr, 0, len(arr)-1, x))


