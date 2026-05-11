"""
1             1
1 2         2 1
1 2 3     3 2 1
1 2 3 4 4 3 2 1

"""

k = 4
for i in range(1, k + 1):
    # 1. Print the left side (ascending)
    for j in range(1, i + 1):
        print(j, end=" ")
    # 2. Print the middle spaces
    # Each row has (k - i) * 2 groups of spaces
    for s in range(1, (k - i) * 2 + 1):
        print(" ", end=" ")
    # 3. Print the right side (descending)
    for a in range(i, 0, -1):
        print(a, end=" ")  
    print() # Move to the next line
