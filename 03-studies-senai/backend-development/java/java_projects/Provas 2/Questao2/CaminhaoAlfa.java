package Questao2;

public class CaminhaoAlfa extends Caminhao{
    static Pluviometro pv = new Pluviometro();

    public String inserePluviometro(double peso, double capacidade) {
        String tipo = "";
        if (peso >= 1000 && capacidade >= 1000000){
            pv.setTipo("Convencional");
            tipo = "Convencioinal";
        }
        else if (peso >= 750 && peso <1000 && capacidade >= 750000){
            pv.setTipo("SemiAutomático");
            tipo = "SemiAutomático";
        }
        else if (peso >= 500 && peso <750 && capacidade >= 500000){
            pv.setTipo("Automático");
            tipo = "Automático";
        }
        return tipo;
    }

}