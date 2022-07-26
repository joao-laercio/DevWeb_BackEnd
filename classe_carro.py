class Carro:
    cor = 'sem cor'
    marca = 'sem marca'
    modelo = 'sem modelo'
    ano = 2010
    km_rodados = 0
    status_motor = 'Desligado'
    status_movimento = 'Parado'
    
    def detalhes(self):
        print ('cor:', self.cor)
        print ('marca:', self.marca)
        print ('modelo:', self.modelo)
        print ('ano:', self.ano)
        print ('km_rodados:', self.km_rodados)
        print ('status_ligar:', self.status_ligar)
        print ('status_desligar:', self.status_desligar)
        print ('status_andar:', self.status_andar)
        print ('status_parar:', self.status_parar)
 
    def adiciona_km_rodados(self, km):
        self.km_rodados = self.km_rodados + km
    
    def ligar(self):
        self.status_motor = 'Ligado'
    
    def desligar(self):
        self.dstatus_motor = 'Desligado'
    
    def andar(self):
        self.status_movimento = 'Andando'
    
    def parar(self):
        self.pstatus_movimento = 'Parado'
        
    def exibir_status(self):
        print('')
        

    

