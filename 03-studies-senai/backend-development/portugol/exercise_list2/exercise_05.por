programa
{
	
	funcao inicio()
	{

		real total_compra, prestacoes, total_prestacoes
		escreva("Digite o valor total da compra: ")
		leia(total_compra)
		
		escreva("\nDigite a quantidade de prestações: ")
		leia(prestacoes)
		
		total_prestacoes = total_compra / prestacoes

		escreva("\nO valor das prestações é de: R$ ", total_prestacoes," reais")
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 294; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */