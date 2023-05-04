from server import Server
from database import database
from fila import fila
import sys
import threading
import select
HOST = '' # vazio indica que podera receber requisicoes a partir de qq interface de rede da maquina
PORT = 10001 # porta de acesso
DB_PATH = '../../data/dic.json'
#define a lista de I/O de interesse (jah inclui a entrada padrao)
entradas = [sys.stdin]

def main():
	'''Inicializa e implementa o loop principal (infinito) do servidor'''
	clientes=[] #armazena as threads criadas para fazer join
	server = Server(HOST,PORT,DB_PATH)
	entradas.append(server.start_server()) # Adiciona o servidor a lista de entradas
	
	print("Pronto para receber conexoes...")
	while True:
		#espera por qualquer entrada de interesse
		leitura, escrita, excecao = select.select(entradas, [], [])
		#tratar todas as entradas prontas
		for pronto in leitura:
			if pronto == server.sock:  #pedido novo de conexao
				clisock, endr = server.aceitaConexao()
				print ('Conectado com: ', endr)
				#cria nova thread para atender o cliente
				cliente = threading.Thread(target=server.atendeRequisicoes, args=(clisock,endr))
				cliente.start()
				clientes.append(cliente) #armazena a referencia da thread para usar com join()
			elif pronto == sys.stdin: #entrada padrao
				cmd = input()
				if cmd == 'fim': #solicitacao de finalizacao do servidor
					for c in clientes: #aguarda todas as threads terminarem
						c.join()
					server.shutdown()
					sys.exit()
				elif cmd == 'hist': #outro exemplo de comando para o servidor
					print(str(server.get_hist.values()))

main()

