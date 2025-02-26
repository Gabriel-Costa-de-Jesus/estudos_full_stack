programa
{
	
	funcao inicio()
	{
 //Faça um algoritmo que leia dois valores inteiros A e B se os valores forem iguais deverá se
//somar os dois, caso contrário multiplique A por B. Ao final de qualquer um dos cálculos deve-se
//atribuir o resultado para uma variável C e mostrar seu conteúdo na tela.

		inteiro a1,b1,c1, soma, multi
		
		
		escreva("Digite o valor de A: ")
		leia(a1)

		escreva("Digite o valor de B: ")
		leia(b1)
		
		se (a1 == b1) {
			soma = a1+b1
			escreva("Soma: ")
			c1 = soma
			escreva(c1)}
		senao {
			multi = a1*b1
			escreva("Multiplicação: ")
			c1 = multi
			escreva(c1)}
			
		
	}
}

/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 489; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */