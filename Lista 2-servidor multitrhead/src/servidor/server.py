#servidor de echo: lado servidor
#com finalizacao do lado do servidor
#com multithreading (usa join para esperar as threads terminarem apos digitar 'fim' no servidor)
import socket
from database import database
import regex as re
import sys
# define a localizacao do servidor

class Server:
		
	def __init__(self,HOST,PORT,db):
		'''Cria um socket de servidor e o coloca em modo de espera por conexoes
		Saida: o socket criado'''
		# cria o socket 
		self.HOST = HOST
		self.PORT = PORT
		self.db_connect =  database(db)

	def start_server(self):

		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Internet( IPv4 + TCP) 
		#Inicializa o banco de dados
		self.db_connect.connect_db() 
		# vincula a localizacao do servidor
		self.sock.bind((self.HOST, self.PORT))
		#armazena historico de conexoes 
		self.conexoes = {}
		# coloca-se em modo de espera por conexoes
		self.sock.listen(5) 

		# configura o socket para o modo nao-bloqueante
		self.sock.setblocking(False)

		# inclui o socket principal na lista de entradas de interesse
		return self.sock

	def aceitaConexao(self):
		'''Aceita o pedido de conexao de um cliente
		Entrada: o socket do servidor
		Saida: o novo socket da conexao e o endereco do cliente'''

		# estabelece conexao com o proximo cliente
		clisock, endr = self.sock.accept()

		# registra a nova conexao
		self.conexoes[clisock] = endr 

		return clisock, endr

	def atendeRequisicoes(self,clisock, endr, lock):
		'''Recebe mensagens e as envia de volta para o cliente (ate o cliente finalizar)
		Entrada: socket da conexao e endereco do cliente
		Saida: '''

		while True:
			#recebe dados do cliente
			data = clisock.recv(1024) 
			print(str(data))
			pack = self.check_requisicao(str(data.decode('utf-8')))
			if type(pack) == str:
				msg = pack
			elif pack[0] == 'POST':
				lock.acquire() #Trava para evitar condições de corrida na escrita
				self.db_connect.insert_pair(pack[1][0],pack[1][1])
				lock.release()
				msg = 'Requisição recebida e cadastrada'
			elif pack[0] == 'GET':
				v = self.db_connect.read_key(pack[1])
				msg = f'Resposta da requisição: {v}'
			elif not data: # dados vazios: cliente encerrou
				print(str(endr) + '-> encerrou')
				clisock.close() # encerra a conexao com o cliente
				return
			
			print(str(endr) + ': ' + str(data, encoding='utf-8'))
			try:
				clisock.send(bytes(msg,'utf-8')) # ecoa os dados para o cliente
			except (BrokenPipeError, IOError):
				print ('Conexão encerrada prematuramente', file = sys.stderr)
				return
			

	def check_requisicao(self,in_):
		'''
		Função de validação de input, checa se a entrada está no formato correto e trata saída
		'''
		match = re.match(r'^(\w+)(?::(.+))?$', in_)
		# print(match.groups())
		if match:
				print(match.groups())
				# Se tiver um segundo grupo não nulo, trata como POST
				if match.groups()[1]!=None:
					word, sentence = match.groups()
					k, v = in_.split(':')
					return ('POST',[k,v]) #Retorna o tipo de operação e o par chave valor
				# Caso contrário, é uma requisição GET
				else:
					k = in_
					return ('GET',k) # Retorna o tipo GET e o valor de consulta
		else:
			return "EROR: Formato de entrada inválido. Use KEY:VALUE para uma inserção ou VALUE para uma consulta"

	def shutdown(self):
		'''
		Desliga o servidor fechando o socket de conexão
		'''
		self.db_connect.persist_db() #Persiste o dicionário
		self.sock.close()

	def get_hist(self):
		return self.conexoes