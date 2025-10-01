class MyStr(str):
    def upper(self):
        print('Chamando upper modificado')
        return super().upper()


s = MyStr('Geek University')

print(s)
print(s.upper())
