package poo.exercise00;

public class ContaPoupanca extends Conta { // Herança uma classe “filha” herda atributos e métodos da “mãe”.
    public ContaPoupanca(String titular, double saldoInicial) {
        super(titular, saldoInicial);
    }

    @Override
    public void imprimirExtrato() { // Polimorfismo - usar o mesmo método de formas diferentes, dependendo da classe.
        System.out.println("Extrato da Conta Poupança de " + getTitular());
        System.out.println("Saldo: " + getSaldo());
    }
}

