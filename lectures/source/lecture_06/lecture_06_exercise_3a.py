temp = []

for i in range(30):
    num = int(input("Δώσε θερμοκρασία: ").strip())
    temp.append(num)

maxThesi = 0
minThesi = 0

for i in range(len(temp)):
    if temp[i] < temp[minThesi]:
        minThesi = i
    if temp[i] > temp[maxThesi]:
        maxThesi = i

print(f"Η max θερμοκρασία είναι {temp[maxThesi]} την ημέρα {maxThesi + 1}")
print(f"Η min θερμοκρασία είναι {temp[minThesi]} την ημέρα {minThesi + 1}")
