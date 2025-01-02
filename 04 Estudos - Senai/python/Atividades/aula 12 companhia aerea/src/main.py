import sys
import os

# Adiciona o caminho da raiz do projeto ao PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.shared_data import lista_aviao, lista_clientes, contador_aviao
from modules.menu_aviao import menu_aviao 
from modules.cadastrar_aviao import cadastrar_aviao
from modules.exibir_informacoes import exibir_informacoes
from modules.cadastrar_cliente import cadastrar_cliente
from modules.cancelar_reserva import cancelar_reserva
from modules.reservas_cadastradas_no_sistema import reservas_cadastradas_no_sistema
from modules.buscar_cliente import buscar_cliente
from modules.alterar_passageiro import alterar_passageiro
from modules.relatorio_de_todas_as_informações_do_sistema import relatorio_de_todas_as_informações_do_sistema
from modules.ranking_voos import gerar_ranking_voos


def main():
    while True:
        opcao = menu_aviao() 
        
        if opcao == 1:
            cadastrar_aviao()
        elif opcao == 2:
            exibir_informacoes()
        elif opcao == 3:
            cadastrar_cliente()
        elif opcao == 4: 
            cancelar_reserva()
        elif opcao == 5:
            reservas_cadastradas_no_sistema()
        elif opcao == 6:
            buscar_cliente()
        elif opcao == 7:
            alterar_passageiro()
        elif opcao == 8:
            relatorio_de_todas_as_informações_do_sistema()
        elif opcao == 9:
            gerar_ranking_voos()
        elif opcao == 10:
            print("Saindo do Sistema...")
            break

if __name__ == "__main__":
    main()
