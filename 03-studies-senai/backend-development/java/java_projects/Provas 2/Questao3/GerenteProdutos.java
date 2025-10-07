package Questao3;

import java.util.ArrayList;

public class GerenteProdutos {
    ArrayList listadeProdutosFabricados = new ArrayList<>();
    ArrayList listadeProdutosComprados  = new ArrayList<>();

    String produto = "Arroz";
    public void Igredientes(String nome){
        listadeProdutosFabricados.add("Arroz");
         System.out.println(listadeProdutosFabricados);
         if (listadeProdutosFabricados.contains(produto)){
             listadeProdutosComprados.add(produto);
         }

    }
    public void ValorCompra(String nome){
        System.out.println(listadeProdutosComprados);
    }
}
