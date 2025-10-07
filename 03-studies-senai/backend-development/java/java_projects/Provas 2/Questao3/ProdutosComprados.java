package Questao3;

public class ProdutosComprados implements IProduto {
    private String nome;
    private float valorDeCompra;
    @Override
    public String getNome() {
        return nome;
    }

    @Override
    public float getCusto() {
        return valorDeCompra;
    }
}
