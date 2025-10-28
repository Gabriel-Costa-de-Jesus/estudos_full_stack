package model;

public class Atendimento {
    String funcionario, dono, pet, data, servico;

    public Atendimento(String funcionario, String dono, String pet, String data, String servico) {
        this.funcionario = funcionario;
        this.dono = dono;
        this.pet = pet;
        this.data = data;
        this.servico = servico;
    }

    @Override
    public String toString() {
        return "\n🔹 DETALHES DO ATENDIMENTO:\n" +
                "----------------------------------------\n" +
                "📅 Data: " + data + "\n" +
                "👨‍⚕️ Funcionário Responsável: " + funcionario + "\n" +
                "----------------------------------------\n" +
                "🐶 Pet Atendido: " + pet + "\n" +
                "👤 Dono do Pet: " + dono + "\n" +
                "----------------------------------------\n" +
                "📝 Serviço/Diagnóstico: " + servico;
    }
}
