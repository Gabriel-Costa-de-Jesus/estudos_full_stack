package Questao4;

import java.util.ArrayList;

public class TodasasDespesas {
    private String cpf;
    ArrayList<Integer> listDespesas = new ArrayList<>();
    private double totalDespesa;

    public String getCpf() {
        return cpf;
    }

    public TodasasDespesas(String cpf) {
        this.cpf = cpf;
    }
    public void totalizaMes(int mes){
        listDespesas.add(mes);
        for (Integer x : listDespesas){
            totalDespesa+= x;
        }
    }
}
