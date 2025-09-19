package interfaces;

public class Cachorro implements Animal{

    public String late(){
       return "Au Au";
    }

    @Override
    public String caminha(){
      return "Andando...";
    }
}
