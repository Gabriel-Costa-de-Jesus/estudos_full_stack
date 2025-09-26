package poo.exercise00;

public abstract class Conta { // Abstração → é o “modelo mental”, você cria classes representando conceitos do mundo real.
    private String titular; //Encapsulamento → esconder os detalhes internos e expor só o necessário (getters/setters).
    private double saldo;

    public Conta(String titular, double saldoInicial) {
        this.titular = titular;
        this.saldo = saldoInicial;
    }

    public String getTitular() {
        return titular;
    }

    public double getSaldo() {
        return saldo;
    }

    public void depositar(double valor) {
        saldo += valor;
    }

    public void sacar(double valor) {
        if (valor <= saldo) {
            saldo -= valor;
        } else {
            System.out.println("Saldo insuficiente!");
        }
    }

    // método abstrato (vai ser implementado de formas diferentes nas subclasses)
    public abstract void imprimirExtrato();
}

