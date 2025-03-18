programa
{
	
	funcao inicio()
	{
		cadeia nome1, nome2
		real idade1, idade2
		inteiro contador 

		nome1= "Chico"
		nome2= "Juca"
		idade1= 1.50
		idade2 = 1.10
		contador = 0

		enquanto (idade2 < idade1) {
			idade1 = idade1 + 0.02
			idade2 = idade2 + 0.03
			
			contador++
			
			} escreva("\nSerão necessários: ", contador, " anos para que Juca seja maior que Chico")

		
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 264; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = {idade1, 7, 7, 6}-{idade2, 7, 15, 6};
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */