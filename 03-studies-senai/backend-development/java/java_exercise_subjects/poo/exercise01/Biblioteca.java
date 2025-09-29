package poo.exercise01;

import java.util.ArrayList;
import java.util.Scanner;

public class Biblioteca {
    ArrayList<MaterialBiblioteca> list = new ArrayList<>();
    public Scanner sc = new Scanner(System.in);

    public void adicionarMaterial(int material){
        System.out.print("\nDigite o título da Obra: ");
        String titulo = sc.nextLine();
        System.out.print("\nDigite o nome do autor: ");
        String autor = sc.nextLine();
        System.out.print("\nDigite o ano da Obra: ");
        int anoPublicacao = sc.nextInt();
        sc.nextLine();

        // list[contador] = new MaterialBiblioteca(titulo, autor, anoPublicacao); FORMA ANTIGA E ERRADA QUE FAZIA
        // list.add(new MaterialBiblioteca(titulo, autor, anoPublicacao)); Forma errada tbm, porque é uma classe Abstrata e apenas filhos podem acessa-la
        if (material == 1){
            list.add(new Livro(titulo, autor, anoPublicacao));
        }
        else if (material == 2){
            list.add(new Revista(titulo, autor, anoPublicacao));
        }
        else if (material == 3){
            list.add(new Jornal(titulo, autor, anoPublicacao));
        }
        System.out.println("\nObra Adicionada Com Sucesso!");
    }
    public void listarMaterias() {
        if(list.isEmpty()){
            System.out.println("\nAdicione algum material Primeiro!");
            return;
        }
//        for (MaterialBiblioteca m : list) {
//            System.out.println(m.getTitulo() + " - " + m.getAutor() + " (" + m.getAnoPublicacao() + ")");
//        }
        for (MaterialBiblioteca m : list) {
            m.exibirDetalhes(); // Versão que só chama a versão específica (Livro, Revista ou Jornal)
        }

    }
    public MaterialBiblioteca buscarPorTitulo(String titulo) {
        for (MaterialBiblioteca m : list) {
            if (m.getTitulo().equalsIgnoreCase(titulo)) {
                System.out.printf("\nA obra [%s] foi encontrada com Sucesso!\n", m.getTitulo());
                return m; // retorna o objeto encontrado
            }
        }
        System.out.println("\nObra não encontrada!");
        return null; // caso não encontre
    }


    public void emprestarMaterial(MaterialBiblioteca material) {
        if (material != null) {
            System.out.println(material.emprestar()); // chama o método da classe abstrata
            list.remove(material); // remove da lista
            System.out.println("Material removido da biblioteca (emprestado).");
        } else {
            System.out.println("Não foi possível emprestar. Material inexistente.");
        }
    }

}
