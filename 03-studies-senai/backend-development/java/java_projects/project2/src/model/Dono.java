package model;

public class Dono extends Pessoa{
    public Dono(String nome, String telefone, String email, String usuario, String senha) {
        super(nome, telefone, email, usuario, senha);
    }

    public Dono() {
    }
    @Override
    public String toString(){
        return "Donos Cadastrados" +
                "----------------------------------------\n" +
                "Nome do Dono: " + getNome();


    }
}
