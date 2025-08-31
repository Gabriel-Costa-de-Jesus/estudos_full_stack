package exercise_list3.exercise04;

public class Carro {
    private double combustivel = 0;
    private double consumo =5;

    public double getCombustivel() {
        return combustivel;
    }
    public void setCombustivel(){
        this.combustivel = combustivel;
    }

    public double getConsumo(){
        return consumo;
    }
    public void setConsumo(){
        this.consumo= consumo;
    }

    public void andar(double distancia){
        this.combustivel -= distancia;
    }
    public void abastecer(double quantidade){
        this.combustivel += quantidade;
    }
}
