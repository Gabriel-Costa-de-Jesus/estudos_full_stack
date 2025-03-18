programa
{
    funcao inicio()
    {
        inteiro n1, quantidade, quantidade_positivo, quantidade_negativo
        real media, soma

        soma = 0.0
        quantidade = 0
        quantidade_positivo = 0
        quantidade_negativo = 0

        faca {
            escreva("Digite um número (0 para sair): ")
            leia(n1)

            se (n1 != 0) {
                soma = soma + n1
                quantidade++

                se (n1 > 0) {
                    quantidade_positivo++
                }
                senao se (n1 < 0) {
                    quantidade_negativo++
                }
            }

        } enquanto (n1 != 0)

        se (quantidade > 0) {
            media = soma / quantidade
        }
        senao {
            media = 0.0
        }

        escreva("\nVocê Saiu do Loop!")
        escreva("\nA Média de todos os números foi: ", media)
        escreva("\nA quantidade de números Positivos foi: ", quantidade_positivo)
        escreva("\nA quantidade de números Negativos foi: ", quantidade_negativo)
    }
}

/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 774; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = {quantidade, 5, 20, 10};
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */