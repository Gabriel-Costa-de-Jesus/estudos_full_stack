bread = int(input("enter quantity of bread sold ")) # Digite a quantidade de pão vendidos
cornbread = int(input("enter quantity of cornbread sold "))

bread = bread*0.12
print(bread)
cornbread = cornbread*1.50
print(cornbread)
total = bread+cornbread
print(f"Total: {total}")
print(f"Save in savings: {total*0.1:.2f} reais") #Mostrar apenas 2 casas decimais
# Guardar na poupança