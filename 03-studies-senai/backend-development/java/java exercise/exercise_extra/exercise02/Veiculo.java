package exercise_extra.exercise02;

public abstract class Veiculo {
    private String modelo, marca;
    private int ano;
    private boolean disponivel;

    public Veiculo(String modelo, String marca, int ano, boolean disponivel){
        this.modelo= modelo;
        this.marca = marca;
        this.ano = ano;
        this.disponivel = disponivel;
    }
    public Veiculo(){}

    public String getModelo(){
        return modelo;
    }
    public void setModelo(String modelo){
        this.modelo = modelo;
    }

    public String getMarca() {
        return marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public int getAno() {
        return ano;
    }

    public void setAno(int ano) {
        this.ano = ano;
    }

    public boolean isDisponivel() {
        return disponivel;
    }

    public void setDisponivel(boolean disponivel) {
        this.disponivel = disponivel;
    }

    public abstract void exibirDetalhes();
}
