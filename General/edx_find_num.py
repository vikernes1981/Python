high = 100
low = 0
middle = (high + low) // 2
print("Please think of a number between 0 and 100!")
while middle <= 100 and middle >= 0:
    print("\nIs your secret number "+str(middle)+"?")
    answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if answer == 'h' or answer == 'l' or answer == 'c':
        if answer == 'h':
            high = middle
            middle = (high + low) // 2
        elif answer == 'l':
            low = middle
            middle = (high + low) // 2
        else:
            print("Game over. Your secret number was: "+str(ans))
            break
    else:
#        while answer != 'h' or answer != 'l' or answer != 'c':
        print("Sorry, I did not understand your input.")
