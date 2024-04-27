def sorting(arr, n):
    low = 0
    mid = 0
    high = len(arr)-1

    while (mid <= high):
        if arr[mid] == 0:
            temp = arr[low]
            arr[low] = arr[mid]
            arr[mid] = temp
            low += 1
            mid += 1

        elif arr[mid] == 2:
            temp = arr[high]
            arr[high] = arr[mid]
            arr[mid] = temp
            high -= 1

        else:
            mid += 1
    return arr


arr_s = int(input())
arr_ele = list(map(int, input().split()))
r = sorting(arr_ele, arr_s)
print(r)
