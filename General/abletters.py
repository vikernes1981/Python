'''
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the 
letters occur in alphabetical order. For example, 
if s = 'azcbobobegghakl', then your program should print

'Longest substring in alphabetical order is: beggh'

In the case of ties, print the first substring. For example, 
if s = 'abcbcd', then your program should print

'Longest substring in alphabetical order is: abc'
'''

s = input("Enter a string : ")
word = ""
word2 = ""
for i in range(len(s)):
    if s[i] >= s[i-1]:
        word += s[i]
        if len(word) > len(word2):
            word2 = word
    else:
        if len(word) > len(word2):
            word2 = word
        word = s[i]
if len(word2) == 0:
    print("Longest substring in alphabetical order is: "+word)
else:
    print("Longest substring in alphabetical order is: "+word2)
        