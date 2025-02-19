programa
{
	
	funcao inicio()
	{

		cadeia nome
		real salario_fixo, total_vendas, percentual_comissao, salario_final, total_comissao 
		
		escreva("Digite seu nome: ")
		leia(nome)

		escreva("Digite seu salário mensal: ")
		leia(salario_fixo)

		escreva("Digite o total de vendas desse mês: ")
		leia(total_vendas)

		escreva("Digite o percentual da comissao em decimal: ")
		leia(percentual_comissao)

		total_comissao =total_vendas * percentual_comissao
		salario_final = salario_fixo + total_comissao 

		escreva("\nFuncionário: ", nome)
		escreva("\nSalário Fixo: ", salario_fixo)
		escreva("\nValor da comissão: ", total_comissao)
		escreva("\nSalário Final: ", salario_final)


		
		
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 317; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */