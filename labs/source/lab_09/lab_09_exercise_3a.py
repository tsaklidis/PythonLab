# Διάβασμα βαθμών
eksamino = []

for i in range(2):
    mathima = []
    for j in range(2):
        # Εισαγωγή δεδομένων
        text = f"Βαθμός εξαμήνου {i+1} και {j+1} μάθημα: "
        vathmos = input(text).strip()
        vathmos = float(vathmos)
        mathima.append(vathmos)
        eksamino.append(mathima)

# Εμφάνιση βαθμών ανά εξάμηνο
print(f"Οι βαθμοί του φοιτητή είναι: {eksamino}")

# Υπολογισμός μέγιστου με βάση το κάθε μάθημα
meg_vathmos = mathima[0]

for mathima in eksamino:
    for i in mathima:
        if meg_vathmos < i:
            meg_vathmos = i

# Εκτύπωση αποτελέσματος
print(f"O μέγιστος βαθμός είναι: {meg_vathmos}")
