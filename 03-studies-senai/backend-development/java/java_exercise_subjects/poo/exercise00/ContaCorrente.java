package poo.exercise00;

public class ContaCorrente extends Conta { // Herança uma classe “filha” herda atributos e métodos da “mãe”.
    public ContaCorrente(String titular, double saldoInicial) {
        super(titular, saldoInicial);
    }

    @Override
    public void imprimirExtrato() { // Polimorfismo - usar o mesmo método de formas diferentes, dependendo da classe.
        System.out.println("Extrato da Conta Corrente de " + getTitular());
        System.out.println("Saldo: " + getSaldo());
    }
}
