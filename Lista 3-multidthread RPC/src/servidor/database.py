import pickle
import json

class BancoDadosDicionario:
    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo
        self.dicionario = dict(self.carregar_dicionario())

    def carregar_dicionario(self):
        try:
            with open(self.caminho_arquivo, 'r') as arquivo:
                return json.load(arquivo)
        except FileNotFoundError:
            return {}

    def salvar_dicionario(self):
        with open(self.caminho_arquivo, 'w') as arquivo:
            json.dump(self.dicionario, arquivo)

    def adicionar_definicao(self, palavra, definicao):
        if palavra in self.dicionario:
            self.dicionario[palavra].append(definicao)
        else:
            self.dicionario[palavra] = [definicao]

    def obter_definicoes(self, palavra):
        return self.dicionario.get(palavra, [])

    def persistir_dicionario(self):
        self.salvar_dicionario()
        print("Dicionário persistido.")