package poo.exercise01;

public class Livro extends MaterialBiblioteca{
    private int numeroPaginas;

    public Livro(String titulo, String autor, int anoPublicacao) {
        super(titulo, autor, anoPublicacao);
    }

//    public Livro(String titulo, String autor, int anoPublicacao, int numeroPaginas) {
//        super(titulo, autor, anoPublicacao);
//        this.numeroPaginas = numeroPaginas;
//    }

    @Override
    public void exibirDetalhes() {
        System.out.println("Livro: " + getTitulo() + " - " + getAutor() + " (" + getAnoPublicacao() + ")");
    }

}
