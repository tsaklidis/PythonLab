# Αρχικοποίηση μεταβλητών
list = []

for i in range(5):
    num = int(input("Δώσε στοιχείο: "))
    list.append(num)

print("H μη ταξινομημένη λίστα είναι:", list)

for i in range(1, 5):
    for j in range(4, i-1, -1):
        if list[j-1] > list[j]:
            temp = list[j-1]
            list[j-1] = list[j]
            list[j] = temp

# Εκτύπωση αποτελέσματος
print("H ταξινομημένη λίστα είναι:", list)
