package exercise_list2.exercise02.Classes;

import java.util.ArrayList;

public class Monkey {
    private String nome;
    private ArrayList<String> estomago;

    public Monkey() {
        estomago = new ArrayList<>();
    }

    public void setCadastrarMonkey(String nome) {
        this.nome = nome;
    }

    public String getNome() {
        return nome;
    }

    public void adicionarComida(String comida) {
        estomago.add(comida);
    }

    public String[] getEstomago() {
        return estomago.toArray(new String[0]);
    }
}
