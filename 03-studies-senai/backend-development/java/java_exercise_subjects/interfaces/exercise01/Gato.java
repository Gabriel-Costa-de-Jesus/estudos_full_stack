package interfaces.exercise01;

public class Gato implements Animal{

    public String mia(){
        return "Miau Miau";
    }

    @Override
    public String caminha(){
        return "Andando...";
    }
}
