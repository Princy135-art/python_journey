n = 5

for row in range(1, n + 1):

    for space in range(n - row):
        print(" ", end="")

    for star in range(2 * row - 1):
        print("*", end="")

    print()