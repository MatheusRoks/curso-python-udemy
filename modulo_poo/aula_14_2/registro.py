from pathlib import Path
import os
import json
from abc import ABC, abstractmethod

LOG_BASE = Path(__file__).parent / "registro.txt"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CAMINHO_ARQUIVO = os.path.join(BASE_DIR, 'Lista_contas.json')


class Registro(ABC):
    @abstractmethod
    def _registrar(self, msg):
        pass

    def registrar_erro(self, msg):
        return self._registrar(f'Erro: {msg}')

    def registrar_sucesso(self, msg):
        return self._registrar(f'Sucesso: {msg}')

    def registrar_saque(self, msg):
        return self._registrar(f'Saque: {msg}')

    def registrar_deposito(self, msg):
        return self._registrar(f'Deposito: {msg}')


class RegistroArquivoMixin(Registro):
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
            return json.load(f) or []


if __name__ == '__main__':
    registro_json = RegistroJson(CAMINHO_ARQUIVO)
    contas = registro_json.carregar_banco()
    print(contas)
