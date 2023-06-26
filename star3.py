for rows in range(1, 5):
    for column in range(1, rows + 1):
        print('*', end=" ")
    print("")

for rows in range(5, 1, -1):
    for column in range(1, rows - 1):
        print('*', end=" ")
    print("")
