class Processo:
    def __init__(self, fila, banco_dados):
        self.fila = fila
        self.banco_dados = banco_dados

    def processar_requisicao(self, requisicao):
        if ':' in requisicao:
            self.processar_registro(requisicao)
            return 'Cadastrado com sucesso'
        else:
            return self.processar_consulta(requisicao)
    def processar_registro(self, requisicao):
        palavra, definicao = requisicao.split(':')
        self.banco_dados.adicionar_definicao(palavra, definicao)

    def processar_consulta(self, requisicao):
        resultado = self.banco_dados.obter_definicoes(requisicao)
        # print(f"Definições para '{requisicao}':")
        # for definicao in resultado:
        #     print(f"- {definicao}")
        return resultado