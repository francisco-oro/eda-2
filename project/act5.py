def relativeSort(A1, A2):
    count = {}
    for num in A1:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    output = []
    for num in A2:
        output.extend([num]*count[num])
        del count[num]

    for num in sorted(count.keys()):
        output.extend([num]*count[num])

    return output

print(relativeSort([2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8], [2, 1, 8, 3]))
