# import (nome do arquivo para ser importado) as (Variável para se conectar ao arquivp e pegar as informações)
 
# Importa o módulo "supermercado" como "sp"
import supermercado as sp

# Chama a função "supermercado_do_povo" do módulo "supermercado"
sp.supermercado_do_povo() # Imprimindo o print do outro arquivo conectado

# Pegando as informações do dicio
print(sp.produtos)
print(sp.produtos["Pimentão"]) # pegnado valor de um só

# --------------------------------

# Importando diretamente
from supermercado import produtos

# Imprimindo apenas o nome
for produto in produtos:
    print(produto)

print("\n")

# Imprimindo apenas os valores
for produto in produtos:
    print(produtos[produto])

# Imprimindo o produto e os valores
for produtos, preco in produtos.items():
    print(produtos, "-", "R$", preco)

# Dicionário multi
departamento = {
    "bebidas" : {
        "Água": 2.00,
        "Refrigerante" : 5.00,
        "Cha": 6.00
    },
    "comidas" : {
        "Pastel" : 4.00,
        "coxinha" : 4.00,
        "Hambuguer" : 4.00
    },
    "frutas" : {
        "banana" : 5.00,
        "Maça" : 3.00
    }
} 