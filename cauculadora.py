
class Cal:
    def __init__(self, resposta = 0):
        self.resposta = resposta
        self.uso = False
        """..."""

    '''@property'''
    def set_resposta(self,nova, tipo):

        if self.resposta == 0:
            self.resposta = nova
        else:
            if tipo == "+":
                self.resposta = self.resposta + nova
            elif tipo == "-":
                self.resposta = self.resposta - nova
            elif tipo == "X":
                self.resposta = self.resposta * nova
            elif tipo == " ":
                self.resposta = self.resposta * nova
        self.uso = True


    def get_resposta(self):
        return self.resposta

    def set_uso(self, novo):
        self.uso = novo

    def get_uso(self):
        return self.uso

