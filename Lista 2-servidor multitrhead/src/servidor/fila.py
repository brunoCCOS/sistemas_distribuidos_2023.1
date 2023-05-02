class fila:
    def __init__(self):
        self.fifo = []
    
    def get_first(self):
        '''
        retorna o primeiro elemento da lista
        '''
        return self.fifo.pop(0)

    def insert_msg(self,msg):
        '''
        Insere uma nova requisição no fim da fila
        '''
        self.fifo.append(msg)
        return
    
    def check_empty(self):
        '''
        Checa se a lista está vazia
        '''
        if self.fifo:
            return False
        else:
            return True
