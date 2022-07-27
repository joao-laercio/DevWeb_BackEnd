from unicodedata import name


class Pessoa(object):
    def __init__(self, nome, idade, endereco, cpf, sexo):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.cpf = cpf
        self.sexo = sexo
       
        
        def resumo(self):
            print ('nome', self.nome)
            print ('idade', self.idade)
            print ('endereco', self.endereco)
            print ('cpf', self.cpf)
            print ('sxo', self.sexo)
            
        def __str__(self):
            return self.name
                
            
class Pai(Pessoa):
    def __init__(self,  nome, idade, endereco, cpf, sexo):
        Pessoa.__init__(self,  nome, idade, endereco, cpf, sexo)
        self.__cpf = cpf
        self.filhos = []
        self.esposa = None
        
    def resumo(self):
        Pessoa.resumo(self)
        print('filhos', self.filhos)
        print('esposa', self.Mae)
        
class Mae(Pessoa):
    def __init__(self,  nome, idade, endereco, cpf, sexo):
        Pessoa.__init__(self,  nome, idade, endereco, cpf, sexo)
        self.__cpf = cpf
        self.filhos = []
        self.esposo = None
        
    def resumo(self):
        Pessoa.resumo(self)
        print('filhos', self.filhos)
        print('esposo', self.Pai)
        
class Filho(Pessoa):
    def __init__(self,  nome, idade, endereco, cpf, sexo):
        Pessoa.__init__(self,  nome, idade, endereco, cpf, sexo)
        self.__cpf = cpf
        self.Pai = Pai()
        self.Mae = Mae()
        
    def resumo(self):
        Pessoa.resumo(self)
        print('Pai', self.Pai)
        print('Mae', self.Mae)
        
        
