n = 5

for row in range(1, n + 1):

    # spaces
    for space in range(n - row):
        print(" ", end="")

    # increasing numbers
    for num in range(1, row + 1):
        print(num, end="")

    # decreasing numbers
    for num in range(row - 1, 0, -1):
        print(num, end="")

    print()