from pathlib import Path
import os
import json


LOG_BASE = Path(__file__).parent / "registro.txt"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CAMINHO_ARQUIVO = os.path.join(BASE_DIR, 'lista_contas.json')


class Registro:
    def _registrar(self, msg):
        raise NotImplementedError('Implemente o metodo registrar')

    def registrar_saque(self, msg):
        return self._registrar(f'Saque: {msg}')

    def registrar_deposito(self, msg):
        return self._registrar(f'Deposito: {msg}')


class RegistroFileMixin(Registro):
    def _registrar(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        with open(LOG_BASE, 'a', encoding="utf-8") as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\n')


class RegistroJson:
    def __init__(self, caminho_arquivo):
        self.caminho = caminho_arquivo

    def salvar_banco(self, lista_clientes):
        dados = [cliente.to_dict() for cliente in lista_clientes]
        with open(self.caminho, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=2, ensure_ascii=False)

    def carregar_banco(self):
        if not os.path.exists(self.caminho):
            return []
        with open(self.caminho, 'r', encoding='utf-8') as f:
            return json.load(f)
