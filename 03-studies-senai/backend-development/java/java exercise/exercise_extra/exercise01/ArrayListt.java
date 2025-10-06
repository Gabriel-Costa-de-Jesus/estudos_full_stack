package exercise_extra.exercise01;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class ArrayListt {
    public static void main(String[] args) {

        // Cria uma lista vazia de pessoas
        ArrayList<String> pessoas = new ArrayList<>();

        // Adiciona elementos no final
        pessoas.add("Fulano");
        pessoas.add("Ciclano");

        // Adiciona "Beltrano" na posição 0 (início)
        pessoas.add(0, "Beltrano");

        // Percorre e imprime todos os nomes
        for (String x : pessoas) {
            System.out.println(x);
        }

        System.out.println("--------------");

        // ❌ Esses métodos não existem em ArrayList — apenas em LinkedList.
        // pessoas.addFirst("Zezinho");
        // pessoas.addLast("Joazinho");

        // Para fazer o mesmo em ArrayList:
        pessoas.add(0, "Zezinho");              // adiciona no início
        pessoas.add(pessoas.size(), "Joazinho"); // adiciona no final

        // Cria uma lista de alunos usando Arrays.asList()
        ArrayList<String> alunos = new ArrayList<>(Arrays.asList("-- Danilo", "Amanda", "Hiago", "Derick"));

        // Adiciona todos os alunos ao final de pessoas
        pessoas.addAll(alunos);

        // Adiciona todos os alunos novamente no início
        pessoas.addAll(0, alunos);

        // Imprime os alunos
        for (String x : alunos) {
            System.out.println(x);
        }

        System.out.println("--------------");

        // Imprime todas as pessoas (lista principal)
        for (String x : pessoas) {
            System.out.println(x);
        }

        // Procura "Amanda" dentro da lista alunos e imprime se encontrar
        String a1 = "Amanda";
        for (int i = 0; i < alunos.size(); i++) {
            if (alunos.get(i).equals(a1))
                System.out.println(a1);
        }

        // Verifica se "pessoas" contém "-- Danilo"
        System.out.println(pessoas.contains("-- Danilo"));

        // Verifica se "pessoas" contém todos os elementos de "alunos"
        System.out.println(pessoas.containsAll(alunos));

        System.out.println("----");

        // Pega o primeiro elemento (índice 0)
        System.out.println(pessoas.get(0));

        // ❌ Esses métodos não existem em ArrayList
        // System.out.println(pessoas.getFirst());
        // System.out.println(pessoas.getLast());

        // ✅ Alternativas corretas:
        System.out.println(pessoas.get(0)); // primeiro
        System.out.println(pessoas.get(pessoas.size() - 1)); // último

        // Mostra índice da primeira e última ocorrência de "-- Danilo"
        System.out.println(pessoas.indexOf("-- Danilo"));
        System.out.println(pessoas.lastIndexOf("-- Danilo"));

        // Verifica se a lista está vazia
        System.out.println(pessoas.isEmpty());

        System.out.println("Lista 2\n");

        // Imprime todos os nomes novamente
        for (String x : pessoas) {
            System.out.println(x);
        }

        System.out.println("\n\n");

        // Remove o elemento do índice 4
        pessoas.remove(4);

        // Remove o nome "Derick" (remove a primeira ocorrência)
        pessoas.remove("Derick");

        // Imprime novamente após remoções
        for (String x : pessoas) {
            System.out.println(x);
        }

        // Verifica se alunos está vazio (false)
        System.out.println(alunos.isEmpty());

        // Remove todos os elementos da lista alunos
        alunos.removeAll(alunos);

        // Verifica se alunos ficou vazio (true)
        System.out.println(alunos.isEmpty());

        // Imprime novamente todas as pessoas
        for (String x : pessoas) {
            System.out.println(x);
        }

        System.out.println("-------Parte 3---------");

        // Cria uma nova lista "invertida" com os mesmos elementos
        List<String> invertida = new ArrayList<>(pessoas);

        // Inverte a ordem da lista
        Collections.reverse(invertida);

        // Mostra lista original e a invertida
        System.out.println(pessoas);
        System.out.println(invertida);

        // Altera o primeiro elemento da lista invertida
        invertida.set(0, "Icaro");

        // Mostra a lista invertida alterada
        System.out.println(invertida);

        System.out.println("------35434-------");

        // Mostra o tamanho da lista de pessoas
        System.out.println(pessoas.size());

        // Mostra a lista completa
        System.out.println(pessoas);

        // Cria uma sublista dos índices 1 a 2 (3 é exclusivo)
        List<String> subLista = pessoas.subList(1, 3);
        System.out.println("Sublista (1,3): " + subLista);

        // Converte a lista para um array
        String[] arrayAlunos = pessoas.toArray(new String[0]);

        // Imprime cada elemento do array
        System.out.println("Elementos do array:");
        for (String nome : arrayAlunos) {
            System.out.println(nome);
        }

        // Limpa a lista de pessoas
        pessoas.clear();

        // Verifica se ficou vazia (true)
        System.out.println(pessoas.isEmpty());
    }
}
