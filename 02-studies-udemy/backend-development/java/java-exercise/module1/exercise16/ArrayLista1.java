package exercise16;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class ArrayLista1 {
    public static void main(String[]args){

        List<String> list = new ArrayList<>();

        list.add("Maria");
        list.add("Alex");
        list.add("Bob");
        list.add("Anna");
        list.add(2, "Marco"); //Acessa a posição 2, coloca o nome Marco e empurra o resto para baixo, sem remover

        System.out.println(list.size());
        for (String x: list) { // Imprime tudo da lista
            System.out.println(x);
        }
        System.out.println("-------------");
        list.remove(2); //Remove a pessoa por indice
        list.remove("Bob"); //Remove a pessoa por nome

        for (String x: list) { // Imprime tudo da lista
            System.out.println(x);
        }
        System.out.println("-------------");
        list.removeIf(x -> x.charAt(0) =='M'); // Remove todos da lista com caractere M

        for (String x: list) { // Imprime tudo da lista
            System.out.println(x);
        }
        System.out.println("-------------");
        System.out.println("Index de Anna" + list.indexOf("Anna"));
        System.out.println("Index de Maria" + list.indexOf("Maria"));
        System.out.println("-------------");
        List<String> result = list.stream().filter(x -> x.charAt(0) == 'A').collect(Collectors.toList()); // Remove tudo da lista e deixa apenas os com letra A
        for (String x: list) { // Imprime tudo da lista
            System.out.println(x);
        }
        System.out.println("-------------");
        String name = list.stream().filter(x -> x.charAt(0) == 'J').findFirst().orElse(null);
        System.out.println(name);
    }
}
