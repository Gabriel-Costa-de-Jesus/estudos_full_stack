from src.models import Class_aviao
from src.shared_data import lista_aviao, contador_aviao

def cadastrar_aviao():
    global contador_aviao
    contador_aviao += 1
    nome_aviao = input("Digite o nome do avião para ser cadastrado: ")
    assentos_aviao = input("Digite a quantidade de assentos do avião: ")
    print(f"\nO avião Nº {contador_aviao}: {nome_aviao} com {assentos_aviao} assentos foi cadastrado com Sucesso!")
    info_aviao = Class_aviao(contador_aviao, nome_aviao, assentos_aviao)
    lista_aviao.append(info_aviao)  