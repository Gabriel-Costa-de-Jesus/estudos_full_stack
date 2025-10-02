package poo.exercise02;

public class VeiculoAVenda {
    private String tipo;
    private String data;
    private double precoDeVenda;

    public VeiculoAVenda(String tipo, String data, double precoDeVenda) {
        this.tipo = tipo;
        this.data = data;
        this.precoDeVenda = precoDeVenda;
    }

    public String getTipo() {
        return tipo;
    }

    public String getData() {
        return data;
    }

    public double getPrecoDeVenda() {
        return precoDeVenda;
    }

    public void veiculoInfo() {
        System.out.printf("Tipo de Veículo: %s%n", tipo);
        System.out.printf("Data do Veículo: %s%n", data);
        System.out.printf("Preço do Veículo: %.2f%n", precoDeVenda);
    }
}
