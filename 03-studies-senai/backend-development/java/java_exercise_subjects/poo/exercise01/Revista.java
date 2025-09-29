package poo.exercise01;

public class Revista extends MaterialBiblioteca{
    private int edicao;

    public Revista(String titulo, String autor, int anoPublicacao) {
        super(titulo, autor, anoPublicacao);
    }

    @Override
    public void exibirDetalhes() {
        System.out.println("Revista: " + getTitulo() + " - " + getAutor() + " (" + getAnoPublicacao() + ")");
    }

}
