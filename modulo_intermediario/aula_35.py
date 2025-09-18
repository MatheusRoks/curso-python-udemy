def add_user(name, lista=None):
    if lista is None:
        lista = []
    lista.append(name)
    return lista


user1 = add_user("Alice")
add_user("Bob", user1)
print(user1)
user2 = add_user("Charlie")
print(user2)
