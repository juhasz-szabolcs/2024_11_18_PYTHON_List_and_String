# Természetesen csak karaktereket tartalmazhatnak!

# Elemeik (a karakterek) nem módosíthatóak!
# Ez hibát okoz:
sztring = 'Ismered ezt a számot?'
sztring[0] = 'i'

# Lista elemek mutable
lista = ['I', 's', 'm', 'e', 'r', 'e', 'd']
lista[0] = 'i'  # Az első elem módosítása
print(lista)  # ['i', 's', 'm', 'e', 'r', 'e', 'd']