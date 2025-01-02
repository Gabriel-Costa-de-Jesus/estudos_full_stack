class Computador: #Nome da classe tem que ser feito com LETRA MAIUSCULA
    def __init__(self):
        self.marca = "Asus" #Informações para ser exibidas
        self.memoria_ram = "8gb"
        self.placa_de_video = "NVDIA"

computador1 = Computador() #Criando uma variável que se conecta a todas as informações dentro da Classe
computador2 = Computador()
computador3 = Computador()

print(computador1.marca,computador1.memoria_ram,computador1.placa_de_video) # Informações para serem acessadas
print(computador2.marca,computador2.memoria_ram,computador2.placa_de_video)
print(computador3.marca,computador3.memoria_ram,computador3.placa_de_video)

#Essa forma no entanto não está correta pois o propósito de uma classe é organizar as informações para que possam ser acessadas fácilmente