package Questao2;

public class Main {
    public static void main(String[] args) {
        CaminhaoAlfa ca = new CaminhaoAlfa();
        CaminhaoBeta cb = new CaminhaoBeta();
        Pluviometro pv = new Pluviometro();

        ca.inserePluviometro( 1009, 1000000);
        System.out.println(ca.inserePluviometro( 999, 6000));

        cb.inserePluviometro(750, 750000);
       // System.out.println(pv.getTipo());
        System.out.println(  cb.inserePluviometro(750, 8000));




    }
}
