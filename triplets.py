def findTriplets(arr, n, K):
    ans = []

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                # If we find a valid triplet.
                if arr[i] + arr[j] + arr[k] == K:
                    triplet = [arr[i], arr[j], arr[k]]
                    # Sorting the triplet to track distinct triplets.
                    triplet.sort()
                    ans.append(triplet)

    return ans


# Example usage:
arr = [1, 2, 3, 4, 5]
n = len(arr)
K = 10
result = findTriplets(arr, n, K)
for triplet in result:
    print(triplet)
