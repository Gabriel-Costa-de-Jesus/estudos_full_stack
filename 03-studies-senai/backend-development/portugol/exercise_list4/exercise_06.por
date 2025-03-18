programa
{
	
	funcao inicio()
	{	
		caracter sexo
		faca {
			escreva("\nDigite seu sexo (Masculino(M) | Feminino(F) | Indefinido(I): ")
			leia(sexo)
			} enquanto (sexo != 'M' e sexo != 'F' e sexo != 'I')
			se (sexo == 'M') {
				escreva("Masculino! Registrado com Sucesso!")}
			senao se (sexo == 'F') {
				escreva("Feminino! Registrado com Sucesso!")}
			senao se (sexo == 'I') {
				escreva("Indefinido! Registrado com Sucesso!")}
			
		
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 438; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */