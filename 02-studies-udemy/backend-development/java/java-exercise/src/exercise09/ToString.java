package exercise09;

import exercise09.*;

import java.util.Scanner;

public class ToString {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);

        Produtos produto = new Produtos();
        System.out.println("Digite o nome do Produto: ");
        produto.nome = sc.nextLine(); // Só é possível fazer isso pq é public
        System.out.println("Digite o preço do Produto");
        produto.preco = sc.nextDouble();
        System.out.println("Quantidade no estoque");
        produto.quantidade = sc.nextInt();

        //System.out.println(produto.toString()); // converte objeto para string, pd usar pra formatar

        System.out.println("Digite a quantidade de produtos para adicionar ao estoque");
        int novaQtd = sc.nextInt();
        produto.addProdutos(novaQtd);

        sc.close();

    }

}
