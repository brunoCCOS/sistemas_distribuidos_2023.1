import json

class database:
    def __init__(self,f_path):
        self.file_path = f_path
        self.open = False
        self.dic = None 

    def coonect_db(self):
        '''
        Lê e desserializa o dicionário da instancia física
        '''
        if not self.open:
            with open(self.file_path, 'r') as jsonFile:
                self.dic = json.load(jsonFile)
                return
        else:
            return
        
    def read_key(self,key):
        '''
        Procura pela chave no dicionário e retorna a lista de valores
        args:
            -key: Chave da busca
        '''
        return self.dic[key]
    
    def insert_pair(self,key,value):
        '''
        Insere o par chave valor no dicionário, ou appenda caso a chave já esteja cadastrada
        args:
            - key: Chave do par
            - value: Valor do campo do dicionário
        '''
        if key in self.dic.keys():
            self.dic[key].append(value)
        else:
            self.dic[key] = [value]

    def persist_db(self):
        with open(self.file_path, 'w') as jsonFile:
            json.dump(self.dic,self.jsonFile)
        return