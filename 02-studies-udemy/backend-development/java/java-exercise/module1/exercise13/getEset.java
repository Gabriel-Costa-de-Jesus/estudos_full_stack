package exercise13;

import java.util.Scanner;

public class getEset {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);


        System.out.println("Digite o nome do Produto: ");
        String nome = sc.nextLine(); // Só é possível fazer isso pq é public
        System.out.println("Digite o preço do Produto");
        double preco = sc.nextDouble();
        
        Produtos produto = new Produtos(nome, preco);// Diferente da instancia normal, está instancia te obriga a passar os valores quando é declarada
        System.out.println(produto.toString()); // converte objeto para string, pd usar pra formatar

        System.out.println("Digite a quantidade de produtos para adicionar ao estoque");
        int novaQtd = sc.nextInt();
        produto.addProdutos(novaQtd);
        System.out.printf("%nForam adicionados %d produtos ao estoque, totalizando %d produtos", novaQtd, produto.getQuantidade());

        System.out.println("\nDigite a quantidade de produtos para remover");
        int removeqtd = sc.nextInt();
        produto.removeProdutos(removeqtd);
        System.out.printf("%nForam removidos %d produtos ao estoque, totalizando %d produtos", removeqtd, produto.getQuantidade());

        produto.setQuantidade(2);
        System.out.printf("\nInfelizmente houve um incendio e acabou queimando todos os produtos, sobrando apenas %d restantes", produto.getQuantidade());
        sc.close();

    }

}
