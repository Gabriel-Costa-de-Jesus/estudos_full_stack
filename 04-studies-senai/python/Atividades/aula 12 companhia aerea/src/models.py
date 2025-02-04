class Class_aviao:
    def __init__(self, numeracao_do_aviao, nome_do_aviao, assentos_do_aviao):
        self.numeracao_do_aviao = numeracao_do_aviao
        self.nome_do_aviao = nome_do_aviao
        # Certificando-se de que assentos_do_aviao é um número inteiro
        self.assentos_do_aviao = int(assentos_do_aviao)  # Converte para inteiro caso seja passado como string

class Class_reserva:
    def __init__(self, aviao_reserva_numero, aviao_reserva_nome, cliente_reserva, assento_reserva):
        self.aviao_reserva_numero = aviao_reserva_numero
        self.aviao_reserva_nome = aviao_reserva_nome
        self.cliente_reserva = cliente_reserva
        self.assento_reserva = assento_reserva
