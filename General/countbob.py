bobcount = 0
omikron = 'o'
beta = 'b'

s = raw_input("Enter a string with 'bob' writen in it : ")

for n in range(len(s)):
    if s[n] == beta:
        if n <= len(s)-3:
            if s[n+1] == omikron:
                if s[n+2] == beta:
                    bobcount += 1
            
print("Number of times bob occurs is: "+ str(bobcount))
