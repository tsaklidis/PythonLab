# Αρχικοποίηση μεταβλητών
max_elements = 10
new_lista = []
lista = []
i = 0

while i < max_elements:
    number = int(input("Δώσε έναν αριθμό: ").strip())
    lista.append(number)
    i += 1

# Αρχικοποίηση μεταβλητών
j = len(lista)

while j > 0:
    new_lista.append(lista[j-1])
    j -= 1

# Εκτύπωση αποτελεσμάτων
print(f"Η νέα λίστα είναι: {new_lista}")
