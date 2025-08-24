package exercise09;

public class Produtos {
    //Apenas para fins didáticos usei public
    public String nome;
    public double preco;
    public int quantidade;

    public double precoTotalEstoque(){
        return preco* quantidade;
    }
    public void addProdutos(int quantidade){ //Setar
        this.quantidade += quantidade;
    }
    public void removeProdutos(int quantidade){ //Setar
        this.quantidade -= quantidade;
    }
    public String toString(){
        return nome
                + ", $"
                + String.format("%.2f", preco)
                + ","
                + quantidade
                + "unidades, Total: $"
                + precoTotalEstoque();
    }
}

