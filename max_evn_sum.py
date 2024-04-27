

def fun(arr):
    pos_odd = []
    neg_od = []
    e_sum = 0

    for i in range(len(arr)):
        e_sum += arr[i]

    if e_sum % 2 == 0:
        return e_sum

    else:
        for i in range(len(arr)):
            if arr[i] > 0 and arr[i] % 2 != 0:
                pos_odd.append(arr[i])

            if arr[i] < 0:
                neg_od.append(arr[i])

        w = min(pos_odd)
        print(w)

        if neg_od:
            y = max(neg_od)
        else:
            y = 0
        print(y)

        g = max(w, y)
        print(g)
        final = e_sum-g

        return final


a = int(input())
arr = list(map(int, input().split()))
print(fun(arr))
