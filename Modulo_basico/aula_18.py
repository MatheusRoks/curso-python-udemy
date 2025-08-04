range_column = 5
range_row = 5

row = 1
while row <=range_row:
    column= 1
    while column <=range_column:
        print(f'{row} {column}|', end=" ")
        column+=1
    print('\n', 23*'_')
    row+=1

