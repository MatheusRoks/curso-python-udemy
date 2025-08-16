
def first_duplicate(lista):
    seen_numbers = set()
    for number in lista:
        if number in seen_numbers:
            return f'A duplicata é {number}'
        seen_numbers.add(number)
    return "Sem duplicatas"

number_list = [
    [1, 2, 3, 4,32, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4,3, 5, 6, 7, 8, 9, 10, 1],
    [1, 2, 3, 4, 5,5, 6,6, 7, 8, 9, 10, 11],
    [1, 2,1, 3, 4, 5, 6, 7, 8, 9, 10, 11,12, 12],
]

for number, nlist in enumerate(number_list):
    print(f'Lista {number+1}: {nlist}')
    print(first_duplicate(nlist))
