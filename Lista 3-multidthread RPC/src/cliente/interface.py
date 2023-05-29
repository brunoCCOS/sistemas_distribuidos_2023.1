class Interface:
    def __init__(self, server):
        self.server = server

    def process_input(self):
        while True:
            command = input("Digite um comando no formato (word) para consulta e (word:sentence) para cadastro: ")
            if not command:
                continue
            if command == 'desligar':
                print('Conexão encerrada')
                return
            else:
                resposta = self.server.adicionar_requisicao(command)
            if type(resposta) == list:
                for defi in resposta:
                    print(defi)
            else:
                print(resposta)