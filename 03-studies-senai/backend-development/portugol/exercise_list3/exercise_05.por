programa
{
	
	funcao inicio()
	{
		inteiro n1,n2,opcao, soma,subtrair,multi,dividir

		escreva("Digite o Primeiro Valor: ")
		leia(n1)
		
		escreva("\nDigite o Segundo Valor: ")
		leia(n2)
		
		escreva("Digite a operação Matemática: ")
		escreva("\n1 - Somar")
		escreva("\n2- Subtrair")
		escreva("\n3- Multiplicar ")
		escreva("\n4- Dividir \n")
		
		leia(opcao)

		se (opcao == 1) {
			escreva("\nVocê escolheu: Somar")
			soma = n1+n2
			escreva("\n",n1," + ", n2, " = ", soma)
			}
		senao se (opcao == 2) {
			escreva("\nVocê escolheu: Subtrair")
			subtrair = n1-n2
			escreva("\n",n1," - ", n2, " = ", subtrair)
			}
		senao se (opcao == 3) {
			escreva("\nVocê escolheu: Multiplicar")
			multi = n1*n2
			escreva("\n",n1," X ", n2, " = ", multi)
			}
		senao se (opcao == 4) {
			escreva("\nVocê escolheu: Dividir")
			dividir = n1/n2
			escreva("\n",n1," / ", n2, " = ", dividir)
			}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 254; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */