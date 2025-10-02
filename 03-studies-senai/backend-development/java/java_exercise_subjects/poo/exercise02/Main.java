package poo.exercise02;

public class Main {
    public static void main(String[] args) {
        MotocicletaAVenda moto = new MotocicletaAVenda("30/09/2025", 18000.0);
        moto.veiculoInfo();

        AutomovelAVenda carro = new AutomovelAVenda("25/08/2005", 28000);
        carro.veiculoInfo();
    }
}

