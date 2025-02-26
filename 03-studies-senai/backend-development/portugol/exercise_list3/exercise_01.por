programa
{
	
	funcao inicio()
	{ //Faça um algoritmo que leia os valores A, B, C e imprima na tela SE a soma de A + B é menor
// que C.
		inteiro a1,b1,c1, soma
		
		
		escreva("Digite o valor de A: ")
		leia(a1)

		escreva("Digite o valor de B: ")
		leia(b1)

		escreva("Digite o valor de C: ")
		leia(c1)
		soma = a1+b1

		escreva(soma)
		
		se (soma < c1) {
			escreva("Este número é menor que C")} 
		senao {
			escreva("Este número é maior que C")}
		
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 468; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */