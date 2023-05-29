import threading
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from fila import *
from database import * 
from processo import *
import time 

class ManipuladorRequisicoes(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

class Atendente(threading.Thread):
    def __init__(self, fila_requisicoes, servidor):
        threading.Thread.__init__(self)
        self.fila_requisicoes = fila_requisicoes
        self.servidor = servidor
        self.status = True

    def run(self):
        while self.servidor.ativo or self.fila_requisicoes.check_vazia():
            requisicao = self.fila_requisicoes.obter_requisicao()
            if requisicao:
                # print(requisicao)
                resposta = self.servidor.processo.processar_requisicao(requisicao[0])
                self.fila_requisicoes.adicionar_resposta(resposta,requisicao[1])
        self.servidor.shutdown()
        

class Servidor:
    def __init__(self, host, porta):
        self.host = host
        self.porta = porta
        self.fila = FilaRequisicoes()
        self.banco_dados = BancoDadosDicionario('./data/dic.json')
        self.processo = Processo(self.fila, self.banco_dados)
        self.thread_servidor = None
        self.servidor = None
        self.ativo = True
        self.clientes_conectados = []

    def adicionar_requisicao(self, requisicao):
        if self.ativo:
            id = self.fila.adicionar_requisicao(requisicao)
            print(id)
            while not self.fila.checar_resposta(id):
                pass
            resposta = self.fila.obter_resposta(id)
            # print(resposta)
            return resposta[0]
        else:
            return 'Servidor não aceita mais requisições'

    def desligar(self):
            self.ativo = False

    def shutdown(self):
            self.banco_dados.persistir_dicionario()
            self.servidor.shutdown()  # Shutdown the XML-RPC server gracefully

    def monitorar_prompt(self):
        while self.ativo:
            comando = input("Digite 'desligar' para desligar o servidor ou 'clientes' para listar os clientes conectados: ")
            if comando.lower() == 'desligar':
                self.desligar()
                break
            elif comando.lower() == 'clientes':
                self.listar_clientes_conectados()

    def listar_clientes_conectados(self):
        print("Clientes conectados:")
        for cliente in self.clientes_conectados:
            print(cliente)

    def iniciar(self):
        self.servidor = SimpleXMLRPCServer((self.host, self.porta), requestHandler=ManipuladorRequisicoes, allow_none=True)
        self.servidor.register_function(self.adicionar_requisicao, 'adicionar_requisicao')
        self.servidor.register_function(self.desligar, 'desligar')
        # self.servidor.register_function(self.obter_clientes_conectados, 'obter_clientes_conectados')
        
        atendente = Atendente(self.fila, self)
        atendente.start()

        # Iniciar uma thread para monitorar o prompt do servidor
        thread_prompt = threading.Thread(target=self.monitorar_prompt)
        print(f"Servidor iniciado em {self.host}:{self.porta}")
        print(f"Atual dicionário de palavras print {self.banco_dados.dicionario}")
        thread_prompt.start()
        
        self.thread_servidor = threading.Thread(target=self.servidor.serve_forever)
        self.thread_servidor.start()

def main():
    server = Servidor('localhost',8000)
    server.iniciar()


if __name__ == '__main__':
    main()