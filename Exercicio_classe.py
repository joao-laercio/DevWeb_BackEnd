class Pessoa(object):
    def __init__(self, nome, idade, endereco, cpf, sexo):
        self.nome = nome
        self.idade = idade
        self.__endereco = endereco
        self.__cpf = cpf
        self.sexo = sexo
       
        
        def resumo(self):
            print ('nome', self.nome)
            print ('idade', self.idade)
            print ('endereco', self.endereco)
            print ('cpf', self.cpf)
            print ('sxo', self.sexo)
            
        
class Pai(Pessoa):
    def __init__(self,  nome, idade, endereco, cpf, sexo):
        Pessoa.__init__(self,  nome, idade, endereco, cpf, sexo)
        self.__cpf = cpf
        self.Filho = []
        self.esposa = Mae()
        
    def resumo(self):
        Pessoa.resumo()
        print('filhos', self.Filho)
        print('esposa', self.Mae)
        
class Mae(Pessoa):
    def __init__(self,  nome, idade, endereco, cpf, sexo):
        Pessoa.__init__(self,  nome, idade, endereco, cpf, sexo)
        self.__cpf = cpf
        self.Filho = []
        self.esposo = Pai()
        
    def resumo(self):
        Pessoa.resumo()
        print('filhos', self.Filho)
        print('esposo', self.Pai)
        
class Filho(Pessoa):
    def __init__(self,  nome, idade, endereco, cpf, sexo):
        Pessoa.__init__(self,  nome, idade, endereco, cpf, sexo)
        self.__cpf = cpf
        self.Filho = []
        self.esposa = Mae()
        
    def resumo(self):
        Pessoa.resumo()
        print('Pai', self.Pai)
        print('Ma', self.Mae)
        
        
