package exercise02;

public class ContaCorrente {
    private int numeroDaConta;
    private String nomeDoTitular;
    private double saldo = 0;

    public ContaCorrente(int numeroDaConta, String nomeDoTitular, double saldo){
        this.numeroDaConta = numeroDaConta;
        this.nomeDoTitular = nomeDoTitular;
        this.saldo = saldo;
    }
    public ContaCorrente(){}

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
