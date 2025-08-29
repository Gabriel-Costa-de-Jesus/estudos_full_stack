package exercise03;

public class ContaInvestimento {
    private int numeroDaConta;
    private String nomeDoTitular;
    private double saldo = 0;

    public ContaInvestimento(int numeroDaConta, String nomeDoTitular, double saldo){
        this.numeroDaConta = numeroDaConta;
        this.nomeDoTitular = nomeDoTitular;
        this.saldo = saldo;
    }
    public ContaInvestimento(){}

    public void depositar(double valor) {
        this.saldo += valor;
    }
    public void sacar(double valor){
        this.saldo -= valor;
    }
    public String toString() {
        return "Conta " + numeroDaConta + " - Titular: " + nomeDoTitular + " - Saldo: " + saldo;
    }
}
