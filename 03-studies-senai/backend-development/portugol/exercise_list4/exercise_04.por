programa
{
	
	funcao inicio()
	{	
		real n1, soma = 0.0, quantidade = 0.0, media
		
		
		
		faca {
			escreva("Digite um número (Para parar o Loop digite 0): ")
			leia(n1)

			
			se (n1 != 0){
				soma = soma + n1
				quantidade++
			}
			
		} enquanto(n1 != 0)

			se (quantidade > 0) {
		           media = soma / quantidade
		           escreva("A soma dos números digitados foi: ", soma)
		           escreva("\nA média dos números digitados foi: ", media)
		     } senao {
		            escreva("Nenhum número válido foi digitado, então não há média.")
        }
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 269; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */