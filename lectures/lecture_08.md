# 8 Λίστες δύο διαστάσεων

---

## Περιεχόμενα

---

- 8.1 Λίστες δύο διαστάσεων
- 8.2 Αποθήκευση στοιχείων
- 8.3 Άθροισμα στοιχείων
- 8.4 Έυρεση MAX
- 8.5 Έυρεση MAX με θέση
- 8.6 Άθροισμα στοιχείων κατά γραμμή
- 8.7 Άθροισμα στοιχείων κατά στήλη
- 8.8 Έυρεση μέγιστου κατά γραμμή
- 8.9 Έυρεση μέγιστου κατά στήλη
- 8.10 Αναζήτηση στοιχείων I
- 8.11 Αναζήτηση στοιχείων II
- 8.12 Ταξινόμηση στοιχείων ανά γραμμή
- 8.13 Ταξινόμηση στοιχείων ανά στήλη
- 8.14 Τετραγωνικός πίνακας
- 8.15 Παραδείγματα
- 8.16 Ασκήσεις

## 8.1 Λίστες δύο διαστάσεων

---

## [8.2 Αποθήκευση στοιχείων](source/lecture_08/lecture_08_example_1.py)

---

```python
ls = []

for i in range(5):
  ypolista = []
  for j in range(4):
    new_num = int(input("Δώσε αριθμό: "))
    ypolista.append(new_num)
  ls.append(ypolista)

print(ls)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_08/lecture_08_example_1.py).

[8.3 Άθροισμα στοιχείων](source/lecture_08/lecture_08_example_2.py)

---

```python
ls = [[2, 3, 4, 1], [7, 3, 3, 9], [6, 5, 5, 8], [1, 9, 4, 1], [0, 4, 7, 4]]

sum = 0

for ypolista in ls:
  for i in ypolista:
    sum += i

print(sum)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_08/lecture_08_example_2.py).

## [8.4 Έυρεση MAX](source/lecture_08/lecture_08_example_3.py)

---

```python
ls = [[2, 3, 4, 1], [7, 3, 3, 9], [6, 5, 5, 8], [1, 9, 4, 1], [0, 4, 7, 4]]

megisto = ls[0][0]

for ypolista in ls:
  for item in ypolista:
    if item > megisto:
      megisto=item

print(megisto)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_08/lecture_08_example_3.py).

## [8.5 Έυρεση MAX με θέση](source/lecture_08/lecture_08_example_4.py)

---

```python
ls = [[2, 3, 4, 1], [7, 3, 3, 9], [6, 5, 5, 8], [1, 9, 4, 1], [0, 4, 7, 4]]

megistoX = 0
megistoY = 0

for x in range(len(ls)):
  for y in range(len(ls[x])):
    if ls[x][y] > ls[megistoX][megistoY]:
      megistoX = x
      megistoY = y

print(megistoX)
print(megistoY)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_08/lecture_08_example_4.py).

## [8.6 Άθροισμα στοιχείων κατά γραμμή](source/lecture_08/lecture_08_example_5.py)

---

```python
ls = [[2, 3, 4, 1], [7, 3, 3, 9], [6, 5, 5, 8], [1, 9, 4, 1], [0, 4, 7, 4]]

for ypolista in ls:
  sumGrammhs = 0
  for item in ypolista:
    sumGrammhs += item

  print("Άθροισμα γραμμής:",sumGrammhs)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_08/lecture_08_example_5.py).

## [8.7 Άθροισμα στοιχείων κατά στήλη](source/lecture_08/lecture_08_example_6.py)

---

```python
ls = [[2, 3, 4, 1], [7, 3, 3, 9], [6, 5, 5, 8], [1, 9, 4, 1], [0, 4, 7, 4]]

for j in range(4):
  sumSthlhs = 0
  for i in range(5):
      sumSthlhs += ls[i][j]
  print("Άθροισμα στήλης:",sumSthlhs)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_08/lecture_08_example_6.py).

## [8.8 Έυρεση μέγιστου κατά γραμμή](source/lecture_08/lecture_08_example_7.py)

---

```python
ls = [[2, 3, 4, 1], [7, 3, 3, 9], [6, 5, 5, 8], [1, 9, 4, 1], [0, 4, 7, 4]]

for ypolista in ls:
  megistoGrammhs = ypolista[0]
  for i in ypolista:
    if megistoGrammhs < i:
      megistoGrammhs = i
  print("Μέγιστο γραμμής:", megistoGrammhs)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_08/lecture_08_example_7.py).

## [8.9 Έυρεση μέγιστου κατά στήλη](source/lecture_08/lecture_08_example_8.py)

---

```python
ls = [[2, 3, 4, 1], [7, 3, 3, 9], [6, 5, 5, 8], [1, 9, 4, 1], [0, 4, 7, 4]]

for j in range(4):
  megistoSthlhs = ls[0][j]
  for i in range(5):
    if megistoSthlhs < ls[i][j]:
      megistoSthlhs = ls[i][j]
  print("Μέγιστο στήλης: ", megistoSthlhs)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_08/lecture_08_example_8.py).

## [8.10 Αναζήτηση στοιχείων I](source/lecture_08/lecture_08_example_9.py)

---

```python
ls = [[2, 3, 4, 1], [7, 3, 3, 9], [6, 5, 5, 8], [1, 9, 4, 1], [0, 4, 7, 4]]

key = int(input("Δώσε στοιχείο που αναζητάς: "))

key_counter = 0

for i in range(5):
  for j in range(4):
    if key == ls[i][j]:
      print(i, j)
      key_counter += 1
print("Βρέθηκε %d φορές." % (key_counter))
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_08/lecture_08_example_9.py).

## [8.11 Αναζήτηση στοιχείων II](source/lecture_08/lecture_08_example_10.py)

---

```python
ls = [[2, 3, 4, 1], [7, 3, 3, 9], [6, 5, 5, 8], [1, 9, 4, 1], [0, 4, 7, 4]]

key = int(input("Δώσε στοιχείο που αναζητάς: "))

key_counter = 0
found = False
i = 0
j = 0

while i < 5 and not found:
  while j < 4 and not found:
    if key == ls[i][j]:
      print(i, j)
      found = True
    j += 1
  i += 1
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_08/lecture_08_example_10.py).

## [8.12 Ταξινόμηση στοιχείων ανά γραμμή](source/lecture_08/lecture_08_example_11.py)

---

```python
A = [[2, 3, 4, 1], [7, 8, 19, 12], [6, 15, 10, 18], [11, 21, 24, 23], [0, -4, -7, 35]]

print("Η μη ταξινομημένη λίστα είναι:", A)

for k in range(5):
  for i in range(1, 4):
    for j in range(3, i-1, -1):
      if A[k][j-1] > A[k][j]:
        temp = A[k][j-1]
        A[k][j-1] = A[k][j]
        A[k][j] = temp
                
print("Η ταξινομημένη λίστα:", A)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_08/lecture_08_example_11.py).

## [8.13 Ταξινόμηση στοιχείων ανά στήλη](source/lecture_08/lecture_08_example_12.py)

---

```python
for k in range(4):
  for i in range(1, 5):
    for j in range(4, i-1, -1):
      if A[j-1][k] > A[j][k]:
        temp = A[j-1][k]
        A[j-1][k] = A[j][k]
        A[j][k] = temp

print("Η ταξινομημένη λίστα:", A)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_08/lecture_08_example_12.py).

## [8.14 Τετραγωνικός πίνακας](source/lecture_08/lecture_08_example_13.py)

---

```python
# Ίδιο πλήθος γραµµών και στηλών
# Άθροισµα Διαγωνίων

sum1 = 0
sum2 = 0

for i in range(4):
  for j in range(4):
    if i == j:
      sum1 += A[i][j]
    if i + j == 3:
      sum2 += A[i][j]
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_08/lecture_08_example_13.py).

## 8.15 Παραδείγματα

---

### [Παράδειγμα 1](source/lecture_08/lecture_08_example_14.py)

```python
A = []

for ypolista in A:
  sum = 0
  for i in ypolista:
    sum += i

A.append(sum)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_08/lecture_08_example_14.py).

### [Παράδειγμα 2](source/lecture_08/lecture_08_example_15.py)

```python
ls = [[1, 2, 3], [1, 1, 1], [2, 3, 4]]
A = [1, 2, 5]
B = []

for key in A:
  counter = 0
  for ypolista in ls:
    for i in ypolista:
      if i == key:
        counter += 1
  B.append(counter)

print(B)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_08/lecture_08_example_15.py).

## 8.16 Ασκήσεις

---

### [Άσκηση 1](source/lecture_08/lecture_08_exercise_1.py)

Για την διαχείριση των βαθµών στο µάθηµα της Πληροφορικής χρησιµοποιείται ένας δισδιάστατος πίνακας µε 20 γραµµές και 4 στήλες. Οι πρώτες τρεις στήλες αντιστοιχούν στους βαθµούς του 1ου, 2ου και 3ου τριµήνου αντίστοιχα και η τέταρτη στήλη στον µέσο όρο. Να γράψετε πρόγραµµα το οποίο να διαβάζει για κάθε ένα από τους 20 µαθητές µιας τάξης τους βαθµούς των τριών τριµήνων. Στη συνέχεια να υπολογίζει τον µέσο όρο. Τέλος, να εµφανίζει αναλυτικά τα στοιχεία του πίνακα για όλους τους µαθητές.

```python
MATHITES = 20
TRIMHNA = 3
list = []

for i in range(MATHITES):
  list.append([])
  sum = 0
  print("\n-------- Μαθητής %d --------" % (i+1))
  for j in range(TRIMHNA):
    vathmos = int(input("Δώσε βαθμό %doυ τριμήνου: " % (i+1)))
    sum += vathmos
    list[i].append(vathmos)
  list[i].append(sum // TRIMHNA)

print('\n', end='')

for g in range(MATHITES):
  print("O μέσος όρος του %dου μαθητή είναι %d." % (g+1, list[g][TRIMHNA]))
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_08/lecture_08_exercise_1.py).

### [Άσκηση 2](source/lecture_08/lecture_08_exercise_2.py)

Μια οµάδα µπάσκετ που αποτελείται από δέκα παίκτες έχει δώσει 15 αγώνες. Να γίνει πρόγραµµα το οποίο θα δέχεται τα ονόµατα των παικτών καθώς και τους πόντους που σηµείωσε κάθε παίκτης σε κάθε αγώνα, θα εµφανίζει τον παίκτη που σηµείωσε τους περισσότερους πόντους καθώς και το σύνολο των πόντων πέτυχε η οµάδα σε κάθε αγώνα.

```python
def athroisma(plist):
  sum = 0
  for item in plist:
    sum += item
  return sum


PAIKTES = 10
AGWNES = 15
pontoi = []
names = []

for i in range(PAIKTES):
  name = input("\nΔώσε το όνομα του %dου παίκτη: " % (i+1))
  names.append(name)
  for j in range(AGWNES):
    pontos = int(input("Δώσε πόντους για τον %do αγώνα: " % (j+1)))
    if (i == 0):
      pontoi.append([])
    pontoi[j].append(pontos)

# Τρέχει για κάθε αγώνα
for agwnas in range(AGWNES):
  # Καλούμε τη συνάρτηση και παίρνουμε το άθροισμα των πόντων ανα αγώνα
  synolo_ponton = athroisma(pontoi[agwnas])
  print("\n-------- Αγώνας %d --------" % (agwnas+1))
  print("Σύνολο πόντων: %d" % (synolo_ponton))
  # Μηδενίζουμε τη θέση του καλύτερου παίκτη
  best_thesi = 0
  # Έστω ο καλύτερος παίκτης με τους περισσότερους πόντους είναι ο πρώτος
  best = pontoi[agwnas][best_thesi]
  # Τρέχει για κάθε παίκτη
  for paiktis in range(PAIKTES):
    if pontoi[agwnas][paiktis] > best:
      best_thesi = paiktis
  print("Καλύτερος παίκτης: %s" % (names[best_thesi]))
  print("Πόντοι καλύτερου παίκτη: %d" % (pontoi[agwnas][best_thesi]))
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_08/lecture_08_exercise_2.py).

[Home](../README.md) | [Lect 1](lecture_01.md) | [Lect 2](lecture_02.md) | [Lect 3](lecture_03.md) | [Lect 4](lecture_04.md) | [Lect 5](lecture_05.md) | [Lect 6](lecture_06.md) | [Lect 7](lecture_07.md) | [Lect 8](lecture_08.md) | [Lect 9](lecture_09.md)