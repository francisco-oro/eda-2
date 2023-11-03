def countPairs(arr, k):
    count = 0
    set_arr = set(arr)

    for num in set_arr:
        if num + k in set_arr:
            count += 1

    return count

print(f'{[1, 5, 3, 4, 2]}:{countPairs([1, 5, 3, 4, 2], 3)}') 
print(f'{[8, 12, 16, 4, 0, 20]}:{countPairs([8, 12, 16, 4, 0, 20], 4)}')  
