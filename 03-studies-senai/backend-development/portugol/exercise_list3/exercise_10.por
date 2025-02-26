programa
{
	
	funcao inicio()
	{
		real salario, financiamento, calc_financiamento
		escreva("Digite seu salário: ")
		leia(salario)
		
		escreva("Digite o financiamento pretendido: ")
		leia(financiamento)

		se (financiamento <= 5 * salario) {
		escreva("Financiamento Concedido")}
		
		senao {
		escreva("Financiamento Negado")
			}
	}
}

/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 341; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */