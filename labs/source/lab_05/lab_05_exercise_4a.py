# Αρχικοποίηση μεταβλητών
numbers = []

num = int(input("Δώσε έναν αριθμό: ").strip())

while num != 0:
    numbers.append(num)
    num = int(input("Δώσε έναν αριθμό: ").strip())

# Αρχικοποίηση μεταβλητών
counter = i = 0

# Εισαγωγή δεδομένων
key = int(input("Δώσε έναν αριθμό που αναζητάς: ").strip())

while i < len(numbers):
    if key == numbers[i]:
        counter += 1
    i += 1

# Εκτύπωση αποτελεσμάτων
print(f"Ο αριθμός {key} έχει εισαχθεί {counter} φορές.")
