
arrays = [[1,1,10,10,9,9,5,5,6,8,8],[1,3,3],[9,9,4]]

[print(f"In array {array}, the number that appears only once is: {i}") for array in arrays for i in array if array.count(i) == 1 ]

################################  OR, BETTER:

from collections import Counter

for array in arrays:
    counts = Counter(array)
    for num, count in counts.items():
        if count == 1:
            print(f"In array {array}, the number that appears only once is: {num}")
