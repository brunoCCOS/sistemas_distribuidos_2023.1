import xmlrpc.client
from interface import *

def main():
    endereco_servidor = 'http://localhost:8000'
    servidor = xmlrpc.client.ServerProxy(endereco_servidor)

    interface = Interface(servidor)
    interface.process_input()

if __name__ == '__main__':
    main()