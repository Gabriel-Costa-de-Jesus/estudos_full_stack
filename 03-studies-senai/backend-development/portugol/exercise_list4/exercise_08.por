programa
{
	
	funcao inicio()
	{
		inteiro n1, multi, guardar, fatorial = 1
		
		escreva("Digite um número Fatorial: ")
		leia(n1)
		guardar = n1
		
		para (inteiro contador = 1; contador < guardar; contador++) {

			fatorial = n1 * contador
			n1 = fatorial // Guardar o novo valor de N1
			
			escreva("\n", guardar, "! X ", contador, " = ", fatorial)
			}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 247; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */