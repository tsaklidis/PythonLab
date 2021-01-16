# 11 Συναρτήσεις I

---

## Περιεχόμενα

- 11.1 Συναρτήσεις
- 11.2 Παραδείγματα
- 11.3 Ασκήσεις

## [11.1 Συναρτήσεις](source/lab_11/lab_11_example_1.py)

---

```python
# Διαβάζουμε έναν αριθμό και ελέγχουμε αν είναι 0 - 10
def readAndCheck():
  goon = True
  while goon:
    num = input("Δώσε αριθμό: ")
    while not num.isdigit():
      num = input("Δώσε αριθμό: ")
    num = int(num)
    if 0 <= num <= 10:
      goon = false
  return num
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_11/lab_11_example_1.py).

## 11.2 Παραδείγματα

---

### 11.2.1 [Παράδειγμα 1(Ταξινόμηση)](source/lab_11/lab_11_example_2.py)

Να γραφεί μια συνάρτηση η οποία θα δέχεται μια λίστα Α με
αριθμούς και θα την ταξινομεί.

```python
def sort(A):
  for i in range(1, len(A)):
    for j in range(len(A)-1, 0, -1):
      if A[j-1] > A[j]:
        temp = A[j-1]
        A[j-1] = A[j]
        A[j] = temp
  return A

list = [5, 7, 8, 9, 3]

x = sort(list[:])
print(x)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_11/lab_11_example_2.py).

### [Παράδειγμα 2](source/lab_11/lab_11_example_3.py)

Να γραφεί ένα πρόγραμμα το οποίο θα διαβάζει (με έλεγχο
ορθότητας) τους βαθμούς 10 μαθητών για δέκα μαθήματα και θα
εκτυπώνει, για κάθε μάθημα τους βαθμούς ταξινομημένους.

```python
# Διαβάζουμε έναν αριθμό και ελέγχουμε αν είναι 0 - 10
def readAndCheck():
  goon = True
  while goon:
    num = input("Δώσε αριθμό: ")
    while not num.isdigit():
      num = input("Δώσε αριθμό: ")
    num = int(num)
    if 0 <= num <= 10:
      goon = False
        
  return num


def sort(A):
  for i in range(1, len(A)):
    for j in range(len(A)-1, 0, -1):
      if A[j-1] > A[j]:
        temp = A[j-1]
        A[j-1] = A[j]
        A[j] = temp
  return A


def readMarks():
  vathmoi=[]
  for i in range(10):
    vathmoi.append(readAndCheck())
  return vathmoi


# MAIN
for i in range(10):
  vathmoi = readMarks()
  print(sort(vathmoi))
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_11/lab_11_example_3.py).

## 11.3 Ασκήσεις

---

### [Άσκηση 1](source/lab_11/lab_11_exercise_1.py)

Να συμπληρωθεί το παρακάτω πρόγραμμα, ώστε:

- να ζητάει από τον χρήστη το πλήθος των ονομάτων που θα
διαβαστούν,
- να υπολογίζει και να εμφανίζει το μήκος του μακρύτερου ονόματος.

```python
# Δεχόμαστε [plithos] ονόματα και τα τοποθετούμε σε λίστα την οποία επιστρέφει
def readNames(plithos):
  onomata = []
  def readNames(plithos):
    onomata = []
  for i in range(plithos):
    onoma = input("Δώσε όνομα:")
    onomata.append(onoma)
  return onomata


def longestName(list):
    maxLength = 0
    for onoma in list:
      if len(onoma) > maxLength:
        maxLength = len(onoma)
  return maxLength


plithos = int(input("Δώσε πλήθος: "))
onomata = readNames(plithos)
x = longestName(onomata)

print("Το μακρύτερο όνομα έχει μήκος:", x)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_11/lab_11_exercise_1.py).

### [Άσκηση 2](source/lab_11/lab_11_exercise_2.py)

Να γραφεί πρόγραμμα το οποίο:

- Θα έχει μια συνάρτηση η οποία θα διαβάζει σε λίστα, Ν βαθμούς
φοιτητών και θα την επιστρεφεί.
- Θα έχει μια συνάρτηση η οποία θα δέχεται μία λίστα και θα
επιστρέφει το μέγιστο στοιχείο της.
- Θα έχει μια συνάρτηση η οποία θα δέχεται μια λίστα και θα
επιστρεφεί τον μέσο όρο των στοιχείων της.
- Θα διαβάζει πόσοι φοιτητές έγραψαν εξετάσεις σε ένα μάθημα.
- Με τη χρήση συνάρτησης θα διαβάζει τους βαθμούς τους.
- Με τη χρήση συνάρτησης θα υπολογιζεί και θα εκτυπώνει τον
μέγιστο βαθμό και τον μέσο όρο.

```python
def readMarks(N):
  marks = []
  for i in range(N):
    mark = int(input("Δώσε βαθμό: "))
    marks.append(mark)
  return marks


def getMax(A):
  megisto = 0
  for i in A:
    if i > megisto:
      megisto = i
  return megisto


def getMO(A):
  souma = 0
  for i in A:
    souma += i
  return souma / len(A)


plithos = int(input("Πόσοι δώσανε το μάθημα:"))

vathmoi = readMarks(plithos)

print("Μέγιστος: ", getMax(vathmoi))
print("Mέσος όρος: ", getMO(vathmoi))
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_11/lab_11_exercise_3.py).

[Home](../README.md) | [Lab 1](lab_01.md) | [Lab 2](lab_02.md) | [Lab 3](lab_03.md) | [Lab 4](lab_04.md) | [Lab 5](lab_05.md) | [Lab 6](lab_06.md) | [Lab 7](lab_07.md) | [Lab 8](lab_08.md) | [Lab 9](lab_09.md) | [Lab 10](lab_10.md)| [Lab 11](lab_11.md)| [Lab 12](lab_12.md)