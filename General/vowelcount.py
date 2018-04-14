vowcount = 0
#vowels = "aeiou"
letters = "qwertyuiopasdfghjklzxcvbnm"

s = raw_input("Enter a string of letters : ")
for letter in s.lower():
    for n in letters:
        if n == letter:
            vowcount += 1

print("Number of vowels: "+ str(vowcount))
