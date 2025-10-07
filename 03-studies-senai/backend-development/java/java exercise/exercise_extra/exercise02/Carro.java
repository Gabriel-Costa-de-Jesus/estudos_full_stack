package exercise_extra.exercise02;

public class Carro extends Veiculo implements Alugavel {
    private int numeroPortas;

    public Carro(String titulo, String autor, int anoPublicacao, boolean disponivel, int numeroPortas){
        super(titulo,autor,anoPublicacao,disponivel);
        this.numeroPortas= numeroPortas;
    }

    public void exibirDetalhes(){

    }


    @Override
    public void alugar() {

    }

    @Override
    public void devolver() {

    }

    @Override
    public boolean estarDisponivel() {
        return false;
    }
}
