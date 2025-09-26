package interfaces.exercise02;

public class Retangulo implements ObjetoGeometrico{
    private double base, altura;

    public Retangulo(double base, double altura){
        this.base = base;
        this.altura = altura;
    }
    @Override
    public double calcularArea(){
        return base*altura;
    }
    @Override
    public double calcularPerimetro(){
        return 2 * (base+altura);
    }
}
