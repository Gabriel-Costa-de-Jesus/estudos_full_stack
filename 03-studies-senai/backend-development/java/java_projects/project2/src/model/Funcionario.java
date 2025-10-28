package model;

public class Funcionario extends Pessoa{
    private String cargo;
    private float salario;

    public Funcionario(String nome, String telefone, String email, String usuario, String senha, String cargo, float salario) {
        super(nome, telefone, email, usuario, senha);
        this.cargo= cargo;
        this.salario= salario;
    }
    public Funcionario(){

    }

    @Override
    public String toString(){
        return "Funcionários Cadastrados" +
                "----------------------------------------\n" +
                "Funcionário: " + getNome() +
                "Cargo: " + cargo +
                "Salário: " + salario +
                "----------------------------------------\n";
    }
}
