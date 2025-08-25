package exercise13;

public class Produtos {
    // Conceito de encapsulamento, deixar tudo private e acessar com get e set
    private String nome;
    private double preco;
    private int quantidade;

    public Produtos(){ // Pode declarar assim tbm

    }

    public Produtos(String nome, double preco, int quantidade){
        this.nome = nome;
        this.preco = preco;
        this.quantidade = quantidade;
    }
    public Produtos(String nome, double preco){ // Isso aqui é uma sobrecarga, é como se fosse o mesmo construtor só que eu botei pra ele receber dois parametros ao inves de três, assim não da erro no código, pq no momento só quero passar dois
        this.nome = nome;
        this.preco = preco;
    }

    // Declarado após os contrutores
    public String getNome(){
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public double getPreco(){
        return preco;
    }
    public void setPreco(double preco){
        this.preco = preco;
    }
    public int getQuantidade(){
        return quantidade;
    }
    public void setQuantidade(int quantidade){
        this.quantidade = quantidade;
    }

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

