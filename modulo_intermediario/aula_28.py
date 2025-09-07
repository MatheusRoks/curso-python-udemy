from itertools import combinations, permutations, product


def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


pessoas = ['joão', 'jose', 'maria', 'matheus', 'paulo']
roupa = [['camisa', 'terno', 'saia'],
         ['preta', 'branca'],
         ['p', 'm', 'g'],
         ['masculina', 'feminina', 'unissex'],
         ]

# print_iter(combinations(pessoas, 2))
# print_iter(combinations(pessoas, 3))
# print_iter(permutations(pessoas, 2))
# print_iter(permutations(pessoas, 3))

print_iter(product(*roupa))
