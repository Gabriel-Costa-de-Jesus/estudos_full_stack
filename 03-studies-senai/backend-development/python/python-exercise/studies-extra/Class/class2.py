class Computador: #Nome da classe  tem que ser feito com LETRA MAIUSCULA
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca #Informações para ser exibidas estão vazias pois o eu direi quando chamar a class
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video

computador1 = Computador("Assus", "4gb", "NVDIA") #Criando uma variável que se conecta a todas as informações dentro da Classe e dando informações que ficaram armazendas na variável
computador2 = Computador("Samsung", "8gb", "AMD")
computador3 = Computador("Lenovo", "16gb", "NVDIA")

print(computador1.marca,computador1.memoria_ram,computador1.placa_de_video) # Informações para serem EXIBIDAS NA TELA
print(computador2.marca,computador2.memoria_ram,computador2.placa_de_video)
print(computador3.marca,computador3.memoria_ram,computador3.placa_de_video)

#Essa forma correta de se fazer, pois as informações podem ser acessadas fácilmente de forma organizada, PORÉM AINDA NÃO É A MELHOR FORMA