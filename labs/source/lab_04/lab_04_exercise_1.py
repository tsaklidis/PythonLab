# Διαβάζουμε από το χρήστη να μας δώσει την 1η ζαριά
zaria1 = input("Δώσε 1η ζαριά: ")
# Διαβάζουμε από το χρήστη να μας δώσει την 2η ζαριά
zaria2 = input("Δώσε 2η ζαριά: ")

# Ελέγχουμε αν αυτό που έγραψε o χρήστης είναι νούμερα.
if zaria1.isdigit() and zaria2.isdigit():
    # Μετατρέπουμε την αλφαριθμητική τιμή σε ακέραια
    zaria1 = int(zaria1)
    zaria2 = int(zaria2)
    # Ελέγχουμε αν τα νούμερα των ζαριών ήταν μεταξύ 1 - 6.
    if (zaria1 >= 1 and zaria1 <= 6) and (zaria2 >= 1 and zaria2 <= 6):
        if zaria1 == 4 and zaria2 == 4:
            print("Ντόρτια")
        elif (zaria1 == 1 and zaria2 == 2) or (zaria1 == 2 and zaria2 == 1):
            print("Ασσόδυο")
        elif zaria1 == zaria2:
            print("Διπλές", zaria1 + zaria2)
        else:
            print(zaria1 + zaria2)
    else:
        print("Γιατί οι ζαριές είναι εκτός ορίων 1 και 6;")
else:
    print("Γιατί έγραψες λέξη;")
