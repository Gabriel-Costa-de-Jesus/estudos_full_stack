package interfaces.exercise01;

public class Cachorro implements Animal{

    public String late(){
       return "Au Au";
    }

    @Override
    public String caminha(){
      return "Andando...";
    }
}
