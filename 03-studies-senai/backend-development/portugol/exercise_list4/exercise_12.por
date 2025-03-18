programa
{
    funcao inicio()
    {
        real altura, maior_altura, menor_altura

        escreva("Digite a altura da pessoa 1: ")
        leia(altura)

        maior_altura = altura
        menor_altura = altura 

        para (inteiro contador = 2; contador <= 5; contador++) {
            escreva("Digite a altura da pessoa ", contador, ": ")
            leia(altura)

            se (altura > maior_altura) {
                maior_altura = altura
            }
            se (altura < menor_altura) {  
                menor_altura = altura
            }
        }

        escreva("\nA menor altura foi: ", menor_altura)
        escreva("\nA maior altura foi: ", maior_altura)
    }
}

/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 70; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */