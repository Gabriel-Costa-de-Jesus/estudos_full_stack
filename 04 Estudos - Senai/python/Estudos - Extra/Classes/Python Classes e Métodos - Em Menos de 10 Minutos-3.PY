class Computador: #Nome da classe  tem que ser feito com LETRA MAIUSCULA
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca 
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video

    def Ligar(self):
        print("Estou ligando")

    def Desligar(self):
        print("Estou Desligando")

    def ExibirInformacoes(self):
        print(self.marca, self.memoria_ram, self.placa_de_video, "\n")


computador1 = Computador("Assus", "4gb", "NVDIA") 
computador2 = Computador("Samsung", "8gb", "AMD")
computador3 = Computador("Lenovo", "16gb", "NVDIA")

computador1.Ligar()
computador1.Desligar()
computador1.ExibirInformacoes()

computador2.Ligar()
computador2.Desligar()
computador2.ExibirInformacoes()

computador3.Ligar()
computador3.Desligar()
computador3.ExibirInformacoes()

#Essa forma correta de se fazer, pois as informações podem ser acessadas fácilmente de forma organizada