programa
{
	
	funcao inicio()
	{

		real peso, altura, imc
		
		escreva("Digite seu peso: ")
		leia(peso)
		
		escreva("Digite sua altura: ")
		leia(altura)

		imc = peso/(altura*altura)

		escreva("\nSeu peso: ", peso)
		escreva("\nSua altura: ", altura, "\n")

		se (imc < 20) {
			escreva("Você está abaixo do peso")
		}
		senao se (imc >= 20 e imc < 25) {
			escreva("Você está com o peso normal")
		}
		senao se (imc >= 25 e imc < 30) {
			escreva("Você está com sobre peso")
		}
		senao se (imc >= 30 e imc <40) {
			escreva("Você está obeso")
		}
		senao se (imc > 40) {
			escreva("Você está Obeso mórbido")
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 265; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */