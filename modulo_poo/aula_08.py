class MyOpen:
    def __init__(self, file_name, mode, encoding='utf-8'):
        self.file_name = file_name
        self.mode = mode
        self.encoding = encoding
        self.file = None

    def __enter__(self):
        print('Abrindo o arquivo')
        self.file = open(self.file_name, self.mode, encoding=self.encoding)
        return self.file

    def __exit__(self, class_exception, exception, traceback):
        print('Fechando o arquivo')
        self.file.close()


if __name__ == '__main__':
    with MyOpen('aula_08.txt', 'w') as arquivo:
        arquivo.write('Linha 1\n')
        arquivo.write('Linha 2\n')
        arquivo.write('Linha 3\n')
