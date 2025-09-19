package interfaces;

public class Gato implements Animal{

    public String mia(){
        return "Miau Miau";
    }

    @Override
    public String caminha(){
        return "Andando...";
    }
}
