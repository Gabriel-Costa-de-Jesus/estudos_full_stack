package poo.exercise01;

public abstract class MaterialBiblioteca {
    private String titulo, autor;
    private int anoPublicacao;

    public MaterialBiblioteca(String titulo, String autor, int anoPublicacao){
        this.titulo= titulo;
        this.autor = autor;
        this.anoPublicacao= anoPublicacao;
    }
    public String getTitulo(){
        return titulo;
    }
    public String getAutor(){
        return autor;
    }
    public int getAnoPublicacao(){
        return anoPublicacao;
    }

    public void setTitulo(String titulo){
        this.titulo=titulo;
    }

    public void setAutor(String autor) {
        this.autor = autor;
    }

    public void setAnoPublicacao(int anoPublicacao) {
        this.anoPublicacao = anoPublicacao;
    }

    public abstract void exibirDetalhes();

    public String emprestar(){
        return "Material Emprestado: " + titulo;
    }
}
