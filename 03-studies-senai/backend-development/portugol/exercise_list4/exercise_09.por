programa
{
	inclua biblioteca Texto --> tx
	
	funcao inicio()
	{
		inteiro n1, n2, opcao, soma, sub, multi, div, total_soma, total_sub, total_multi, total_div, contador, guardar
		cadeia sair, sair_formatado1, limpar, limpar_formatado1

		total_soma = 0
		total_sub = 0
		total_multi = 1  // Inicializa com 1 para evitar multiplicação por 0
		total_div = 0
		contador = 0
		n1 = 0
		guardar = 0
		
		faca {
			se (contador == 0) {
				escreva("\nDigite um número: ")
				leia(n1)
				guardar = n1  // Inicializa o guardar com o valor de n1
			}
				
			escreva("Escolha uma operação matemática: ")
			escreva("\n1 - Somar")
			escreva("\n2 - Subtrair")
			escreva("\n3 - Multiplicar")
			escreva("\n4 - Dividir\n")
			leia(opcao)
	
			escreva("\nDigite outro número: ")
			leia(n2)

			se (opcao == 1) {
				soma = guardar + n2
				total_soma = soma
				escreva("Total = ", total_soma)
				guardar = total_soma  // Atualiza o guardar com o total da soma
			}
			
			senao se (opcao == 2) {
				sub = guardar - n2
				total_sub = sub
				escreva("Total = ", total_sub)
				guardar = total_sub  // Atualiza o guardar com o total da subtração
			}
			
			senao se (opcao == 3) {
				multi = guardar * n2
				total_multi = multi
				escreva("Total = ", total_multi)
				guardar = total_multi  // Atualiza o guardar com o total da multiplicação
			}
			
			senao se (opcao == 4) {
				se (n2 == 0) {
					escreva("Erro! Divisão por zero não permitida.\n")
				} senao {
					div = guardar / n2
					total_div = div
					escreva("Total = ", total_div)
					guardar = total_div  // Atualiza o guardar com o total da divisão
				}
			}
			
			senao {
				escreva("\nOpção inválida! Digite um número de 1 a 4.\n")
			}
	
			// Tratamento da saída
			escreva("\nVocê quer sair? (Sim/Não): ")
			leia(sair)

			sair_formatado1 = tx.caixa_alta(sair)
			sair_formatado1 = tx.substituir(sair_formatado1, "NÃO", "NAO")
			sair_formatado1 = tx.substituir(sair_formatado1, "N", "NAO")
			sair_formatado1 = tx.substituir(sair_formatado1, "S", "SIM")

			// Tratamento da limpeza de valores
			escreva("\nVocê deseja limpar os valores? (Sim/Não): ")
			leia(limpar)

			limpar_formatado1 = tx.caixa_alta(limpar)
			limpar_formatado1 = tx.substituir(limpar_formatado1, "NÃO", "NAO")
			limpar_formatado1 = tx.substituir(limpar_formatado1, "N", "NAO")
			limpar_formatado1 = tx.substituir(limpar_formatado1, "S", "SIM")

			// Contador
			contador++
		
			// Resetando os valores se o usuário escolher limpar
			se (limpar_formatado1 == "SIM") {
				total_soma = 0
				total_sub = 0
				total_multi = 1
				total_div = 0
				contador = 0
				guardar = 0
				n2 = 0
			}

			
		
		} enquanto(sair_formatado1 != "SIM")

		escreva("\nPrograma Encerrado!")
	}
}

/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 2487; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */