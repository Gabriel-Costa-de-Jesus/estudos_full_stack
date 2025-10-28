package service;

import model.*;

import java.util.ArrayList;
import java.util.List;


public class Clinica {
    private List<Funcionario> funcionarios = new ArrayList<>();
    private List<Dono> donos = new ArrayList<>();
    private List<Animal> animais = new ArrayList<>();
    private List<Atendimento> atendimentos = new ArrayList<>();

    public void cadastrarFuncionario(Funcionario f){
        funcionarios.add(f);
    }
    public void cadastrarDono(Dono d){
        donos.add(d);
    }
    public void cadastrarAnimal(Animal a){
        animais.add(a);
    }

    public List<Funcionario> getFuncionarios(){
        return funcionarios;
    }
    public List<Dono> getDonos(){
        return donos;
    }
    public List<Animal> getAnimais() {
        return animais;
    }
    public List<Atendimento> getAtendimentos() {
        return atendimentos;
    }

    public boolean associarDono(String buscarDono){
        return donos.contains(buscarDono);
    }
    public void registrarAtendimento(Atendimento at){
        atendimentos.add(at);
    }

    public void getImprimirFuncionario(){
        for (Funcionario f: funcionarios){
            System.out.println(f);
            System.out.println("-------------------------------");
        }
    }
    public void getImprimirDonos(){
        for (Dono d: donos){
            System.out.println(d);
            System.out.println("-------------------------------");
        }
    }
    public void getImprimirAnimal(){
        for (Dono a: donos){
            System.out.println(a);
            System.out.println("-------------------------------");
        }
    }
    public void getImprimirAtendimento(){
        for (Atendimento at: atendimentos){
            System.out.println(at);
            System.out.println("-------------------------------");
        }
    }

}
