def get_subarrays_of_length(arr, length):
    subarrays = []
    n = len(arr)

    # Check if the specified length is valid
    if length > n:
        return "Error: Specified length is greater than the length of the array"

    # Iterate over each index of the array
    for start in range(n - length + 1):
        subarray = arr[start:start + length]
        subarrays.append(subarray)

    return subarrays


# # Example usage:
# arr = [1, 2, 3, 4, 5]
# length = 3
# subarrays = get_subarrays_of_length(arr, length)
# print("Subarrays of length", length, ":", subarrays)


def min_subarray(p):
    min_values = []
    for i in p:
        if i[0] < i[1]:
            min_values.append(i[0])
        elif i[0] > i[1]:
            min_values.append(i[1])

    return min_values


def max_elements(q):
    max = q[0]
    for i in q:
        if i > max:
            max = i
    return max


array = [3, 1, 4, 6, 2, 5]
length = 2
b = get_subarrays_of_length(array, length)
print(b)
c = min_subarray(b)
print(c)
d = max_elements(c)
print(d)
