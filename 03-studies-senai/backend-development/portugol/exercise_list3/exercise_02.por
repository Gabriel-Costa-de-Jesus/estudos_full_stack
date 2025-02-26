programa
{

	inclua biblioteca Texto --> t
	
	funcao inicio()
	{
	// Faça um algoritmo que leia o nome, o sexo e o estado civil de uma pessoa. Caso sexo seja “F” e
// estado civil seja “CASADA”, solicitar o tempo de casada (anos).

		cadeia nome, sexo, estado_civil
		
		escreva("Digite seu nome: ")
		leia(nome)

		escreva("\nDigite seu sexo: ")
		leia(sexo)

		escreva("\nDigite seu estado Civil: ")
		leia(estado_civil)

		escreva("\nNome: ", nome)
		escreva("\nSexo: ", sexo)
		escreva("\nCivil: ", estado_civil)

		se (t.caixa_baixa(sexo) == "f" e t.caixa_baixa(estado_civil) == "casada") {
			escreva("Olá CASADA!")
			escreva("\nA quanto tempo você está casada?")
			}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 641; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */