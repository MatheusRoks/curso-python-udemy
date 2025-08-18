def generator(n=0, maxim=10):
    while True:
        yield n
        if n>=maxim:
            return "Termino mizeravi"
        n+=1

gen = generator()
for n in gen:
    print(n)

def gera1():
    yield 1
    yield 2
    yield 3

def gera2():
    yield from gera1()
    yield 4
    yield 5
    yield 6 
    yield 7

gerado = gera2()
for n in gerado:
    print(n)