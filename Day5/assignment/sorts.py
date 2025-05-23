lists = [1, 2, 3, 4, 2, 3, 5, 6, 1, 7, 3]

#bubble sort
for index in range(len(lists) ):

    if lists[index] > lists[index + 1]:
        lists[index] = lists[index + 1]

print(lists)

