programa
{
	
	funcao inicio()
	{

		real custo, porcentagem, lucro, valor_venda
		
		escreva("Digite o preço de custo do produto: ")
		leia(custo)

		escreva("\nDigite em porcentagem o lucro que deseja ser obitido pelo produto: ")
		leia(porcentagem)
		
		lucro = custo * porcentagem
		valor_venda = custo + lucro

		escreva("\nSeu lucro será de: R$ ", lucro, " reais")
		escreva("\nO preço de venda é de: R$ ", valor_venda, " reais")
		
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 423; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */