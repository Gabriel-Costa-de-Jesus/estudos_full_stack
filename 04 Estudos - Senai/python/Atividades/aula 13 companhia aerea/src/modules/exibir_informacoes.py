from src.models import Class_aviao
from src.shared_data import lista_aviao

def exibir_informacoes():
    print("--"*30)
    for info_aviao in lista_aviao:
        print(f"Númeração do avião: {info_aviao.numeracao_do_aviao}\n"
              f"Nome do Avião: {info_aviao.nome_do_aviao} \n"
              f"Quantidade de Assentos Disponíveis: {info_aviao.assentos_do_aviao} assentos \n")
    print("--"*30) 