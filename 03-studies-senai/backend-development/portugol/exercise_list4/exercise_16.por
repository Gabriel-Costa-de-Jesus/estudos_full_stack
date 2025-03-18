programa
{
    funcao inicio()
    {
        cadeia nome, sair, nome_da_pessoa_com_maior_salario
        real salario, media_salario, total_salario, maior_salario, valor_da_pessoa_com_maior_salario
        real percentual_salario, quantidade_salario_ate_1000
        inteiro contador, filhos, media_filhos, total_filhos

        // Inicialização de variáveis
        total_salario = 0.0
        total_filhos = 0
        contador = 0
        maior_salario = 0.0
        valor_da_pessoa_com_maior_salario = 0.0
        quantidade_salario_ate_1000 = 0.0
        nome_da_pessoa_com_maior_salario = " "

        faca {
            escreva("Digite o nome da Pessoa: ")
            leia(nome)
            
            escreva("\nDigite seu salário: ")
            leia(salario)

            escreva("\nDigite a quantidade de filhos: ")
            leia(filhos)

            escreva("\nVocê deseja sair do Programa? (SIM / Nao) ")
            leia(sair)

            // Contador de pessoas
            contador++

            // Somar os valores para cálculo da média
            total_salario = total_salario + salario
            total_filhos = total_filhos + filhos

            // Verificar maior salário
            se (salario > maior_salario) {
                maior_salario = salario
                nome_da_pessoa_com_maior_salario = nome
                valor_da_pessoa_com_maior_salario = salario
            }

            // Contar pessoas com salário até R$1000,00
            se (salario <= 1000) {
                quantidade_salario_ate_1000++
            }

        } enquanto (sair != "SIM" e sair != "sim")

        // Cálculo das médias
        se (contador > 0) {
            media_salario = total_salario / contador
            media_filhos = total_filhos / contador
            percentual_salario = (quantidade_salario_ate_1000 / contador) * 100
      
        // Só para verificar se a pessao digitou algo
        }
        senao {
            media_salario = 0.0
            media_filhos = 0
            percentual_salario = 0.0
        }

        // Exibir resultados
        escreva("\nVocê Saiu do Loop!")
        escreva("\nA Média de salário foi: ", media_salario)
        escreva("\nA Média de filhos foi: ", media_filhos)
        escreva("\nA Pessoa com maior salário foi: ", nome_da_pessoa_com_maior_salario, " com R$ ", valor_da_pessoa_com_maior_salario)
        escreva("\nPercentual de pessoas com salário até R$ 1000,00: ", percentual_salario, "%")
    }
}

/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 1860; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */