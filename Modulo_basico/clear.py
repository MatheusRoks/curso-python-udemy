import os

''' limpeza do terminal'''
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

