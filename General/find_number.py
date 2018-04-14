import random

n = random.randint(0, 100)
counter = 0

print("\nΓια να τερματίσεις το παιχνίδι πρέπει :\n\n1)Nα βρεις τον σωστό αριθμό ή\n2)Nα πατήσεις X\n")
while True:
    choice = input("Διαλεξε εναν αριθμό από το 1 εώς το 100 ή πάτα 'Χ' για έξοδο : ")
    if choice.isdigit():
        choice = int(choice)
        if choice < n and choice > 1 and (choice <= 100 and choice >= 1):
            counter += 1
            print("ΟΧΙ είναι μεγαλύτερος")
        elif choice > n  and choice > 1 and (choice <= 100 and choice >= 1):
            counter += 1
            print("ΟΧΙ είναι μικρότερος")
        elif choice == n:
            counter += 1
            print("Το βρήκατε σωστά μετά από {} προσπάθειες".format(counter))
            print("Σας ευχαριστούμε που παίξατε.")
            break
        elif choice < 1:
            counter = counter
            print("Δοκίμασε έναν αριθμό από το 1 εώς το 100 παρακαλώ!")
    elif choice.isalpha():
        if choice == 'x' or choice == 'X' or choice == 'χ' or choice == 'Χ' :
            choice.upper()
            print("Σας ευχαριστούμε που παίξατε.")
            break
        elif choice.isalpha() and counter == 0:
            counter = 0
            print("Μόνο νούμερα ή το 'Χ' επιτρέπονται!")
        else:
            counter = counter
            print("Μόνο νούμερα ή το 'Χ' επιτρέπονται!")
    else:
        print("Δοκίμασε έναν αριθμό από το 1 εώς το 100 παρακαλώ!")
        if counter == 0:
            counter = 0
        else:
            counter = counter