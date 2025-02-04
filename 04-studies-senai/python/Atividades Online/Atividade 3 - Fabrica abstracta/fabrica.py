# Classe abstrata
class MetodoDePagamento:
    def tipo_de_pagamento(self):
        pass  # As subclasses devem implementar este método

# Subclasses
class Credito(MetodoDePagamento):
    def tipo_de_pagamento(self):
        return "Crédito"

class Boleto(MetodoDePagamento):
    def tipo_de_pagamento(self):
        return "Boleto"

class Pix(MetodoDePagamento):
    def tipo_de_pagamento(self):
        return "Pix"

# Fábrica
def escolha_do_pagamento(escolha):
    if escolha.lower() == "credito":
        return Credito()
    elif escolha.lower() == "boleto":
        return Boleto()
    elif escolha.lower() == "pix":
        return Pix()
    else:
        raise ValueError("Escolha inválida! Opções: Crédito, Boleto ou Pix")

# Utilizando a fábrica
escolha = input("Digite o método de pagamento (Crédito, Boleto, Pix): ")

metodo = escolha_do_pagamento(escolha)
print(f"Você escolheu {metodo.tipo_de_pagamento()} como método de pagamento")

# Teste

# pagamento_credito = credito()
# pagamento_boleto = boleto()
# pagamento_pix = pix()

# print("Tipo de pagamento:", pagamento_credito.tipo_de_pagamento())
# print("Tipo de pagamento:", pagamento_boleto.tipo_de_pagamento())
# print("Tipo de pagamento:", pagamento_pix.tipo_de_pagamento())