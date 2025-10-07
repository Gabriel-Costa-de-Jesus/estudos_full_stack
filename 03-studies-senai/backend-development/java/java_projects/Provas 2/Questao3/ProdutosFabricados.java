package Questao3;


import java.util.ArrayList;

public class ProdutosFabricados implements IProdutoFabricado {
    private String nome;
    ArrayList<String> listadeIngrediente = new ArrayList<>();

    @Override
    public int getNumeroIngredientes() {
        return 0;
    }

    @Override
    public IProduto getigrediente(int numero) {
        return null;
    }

    @Override
    public String getNome() {
        return "";
    }

    @Override
    public float getCusto() {
        return 0;
    }
}
