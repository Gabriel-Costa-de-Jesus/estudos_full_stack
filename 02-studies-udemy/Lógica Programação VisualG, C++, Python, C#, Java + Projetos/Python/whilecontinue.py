contador = 0

while contador < 10:
    contador += 1
    
    if contador == 5:
        continue # Ele não irá ler a linha de baixo e irá para cima
    print(f"Número: {contador}")