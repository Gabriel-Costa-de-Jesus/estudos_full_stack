package poo.exercise01;

public class Jornal extends MaterialBiblioteca{
    private String dataEdicao;

    public Jornal(String titulo, String autor, int anoPublicacao) {
        super(titulo, autor, anoPublicacao);
    }

    @Override
    public void exibirDetalhes() {
        System.out.println("Jornal: " + getTitulo() + " - " + getAutor() + " (" + getAnoPublicacao() + ")");
    }

}
