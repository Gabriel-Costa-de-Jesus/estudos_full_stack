import unicodedata # Biblioteca em Python util para formatação de texto

# Funções úteis de formatação
def remover_acentos(texto):
    # Normaliza o texto para 'NFD', que separa caracteres e seus acentos
    texto_normalizado = unicodedata.normalize('NFD', texto)
    # Filtra apenas os caracteres que não são acentos
    texto_sem_acentos = ''.join(
        c for c in texto_normalizado if unicodedata.category(c) != 'Mn'
    )
    return texto_sem_acentos

def deixar_maiusculo(texto):
    return texto.upper()

def deixar_minusculo(texto):
    return texto.lower()

def capitalizar_inicial(texto):
    return texto.capitalize()  # Apenas a primeira letra em maiúsculo

def remover_espacos_extras(texto):
    return ' '.join(texto.split())  # Remove espaços extras no início, fim e duplicados no meio

# Frase de exemplo
texto = "   OlÁ,  muNdo!  Python é fÁcil.   " # Dato bruto para ser formatado

print(f"Texto original: '{texto}'\n")

# Aplicando as formatações
texto_sem_espacos = remover_espacos_extras(texto)
print(f"Sem espaços extras: '{texto_sem_espacos}'")

texto_minusculo = deixar_minusculo(texto_sem_espacos)
print(f"Minúsculo: '{texto_minusculo}'")

texto_maiusculo = deixar_maiusculo(texto_sem_espacos)
print(f"Maiúsculo: '{texto_maiusculo}'")

texto_capitalizado = capitalizar_inicial(texto_sem_espacos)
print(f"Primeira letra maiúscula: '{texto_capitalizado}'")

texto_sem_acentos = remover_acentos(texto_minusculo)
print(f"Sem acentos: '{texto_sem_acentos}'")
