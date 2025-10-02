package poo.exercise02;

public class AutomovelAVenda extends VeiculoAVenda {
    private static final String TIPO = "Automóvel";

    public AutomovelAVenda(String data, double precoDeVenda) {
        super(TIPO, data, precoDeVenda);
    }

}

// exemplo de package poo.exercise02;
//
//public class AutomovelAVenda extends VeiculoAVenda {
//    // construtor da subclasse
//    public AutomovelAVenda(String data, double precoDeVenda) {
//        // passa "Automóvel" fixo como tipo
//        super("Automóvel", data, precoDeVenda);
//    }
//}