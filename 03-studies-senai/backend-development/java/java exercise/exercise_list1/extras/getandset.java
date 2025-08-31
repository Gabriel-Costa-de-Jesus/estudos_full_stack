package exercise_list1.extras;

public class getandset {
    public static class Pessoa { // Quando coloca Static signfica que é para o mesmo arquivo, interno
        // Declaração de atributos e variáveis
        private String nome;
        private int idade;

        //Getter para nome
        public String getNome(){
            return nome;
        }

        // Setter para nome
        public void setNome(String novoNome) {
            nome = novoNome;
        }

        // Getter para 'idade'
        public int getIdade() {
            return idade;
        }

        // Setter para 'idade'
        public void setIdade(int novaIdade) {
            if (novaIdade >= 0) { // podemos colocar regras
                idade = novaIdade;
            }
        }
    }
    public static void main(String[]args) {
        Pessoa p = new Pessoa();

        // Usando setters para definir valores
        p.setNome("Gabriel");
        p.setIdade(21);

        // Usando getters para ler valores
        System.out.println("Nome: " + p.getNome());
        System.out.println("Idade: " + p.getIdade());
    }
}