range_column = 5
range_row = 5

for row in range(range_row):
    for column in range(range_column):
        print(f'{row+1} {column+1}|', end=" ")
    print('\n', 23*'_')

