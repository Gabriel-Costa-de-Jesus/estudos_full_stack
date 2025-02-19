programa
{
	
	funcao inicio()
	{
		real n1, n2, n3, media
		cadeia nome

		escreva("Digite seu nome: ")
		leia(nome)

		escreva("\nDigite a nota da primeira unidade: ")
		leia(n1)

		escreva("\nDigite a nota da segunda Unidade: ")
		leia(n2)

		escreva("\nDigite a nota da terceira unidade: ")
		leia(n3)

		media = (n1+n2+n3)/3

		escreva("\nParabéns ", nome, " Sua média foi: ", media)

		se (media >= 7) {
			escreva("\nVocê foi aprovado com Sucesso!")		
		}
		senao {
			escreva("\nVocê foi reprovado")
		}

		
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 136; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */