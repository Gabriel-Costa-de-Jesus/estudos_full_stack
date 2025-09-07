package exercise11;

import java.util.Scanner;

public class Construtor {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);


        System.out.println("Digite o nome do Produto: ");
        String nome = sc.nextLine(); // Só é possível fazer isso pq é public
        System.out.println("Digite o preço do Produto");
        double preco = sc.nextDouble();
        System.out.println("Quantidade no estoque");
        int quantidade = sc.nextInt();
        Produtos produto = new Produtos(nome, preco, quantidade);// Diferente da instancia normal, está instancia te obriga a passar os valores quando é declarada
        //System.out.println(produto.toString()); // converte objeto para string, pd usar pra formatar

        System.out.println("Digite a quantidade de produtos para adicionar ao estoque");
        int novaQtd = sc.nextInt();
        produto.addProdutos(novaQtd);
        System.out.printf("%nForam adicionados %d produtos ao estoque, totalizando %d produtos", novaQtd, produto.quantidade);

        System.out.println("\nDigite a quantidade de produtos para remover");
        int removeqtd = sc.nextInt();
        produto.removeProdutos(removeqtd);
        System.out.printf("%nForam removidos %d produtos ao estoque, totalizando %d produtos", removeqtd, produto.quantidade);

        sc.close();

    }

}
