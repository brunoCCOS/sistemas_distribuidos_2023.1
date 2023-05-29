class FilaRequisicoes:
    def __init__(self):
        self.id = 0 # contador único
        self.requisicoes = []
        self.respostas = {}

    def adicionar_requisicao(self, requisicao):
        self.id += 1
        self.requisicoes.append([requisicao,self.id])
        return self.id

    def obter_requisicao(self):
        try:
            return self.requisicoes.pop(0)
        except IndexError  as e:
            pass

    def adicionar_resposta(self, resposta,id):
        self.respostas[id] = resposta,id
        
    def obter_resposta(self,id):
        if self.respostas:
            return self.respostas.pop(id)
        else:
            return None
        
    def checar_resposta(self,id):
        if id in self.respostas.keys():
            return True
        else:
            return False
    
    def check_vazia(self):
        if self.requisicoes:
            return True
        else: 
            return False