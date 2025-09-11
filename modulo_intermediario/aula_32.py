def recursiva(ini=0, fim=100):
    if ini >= fim:
        return fim
    ini += 1
    return recursiva(ini, fim)


print(recursiva())
