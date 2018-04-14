letters = "qwertyuiopasdfghjklzxcvbnm"
counter = {}
count = 0

try:
	fname = input("Give name of file : ")
	with open(fname, 'r', encoding='utf-8') as fin:
		txt = fin.read()
		for i in txt.lower().replace(" ", ""):
			if i not in counter:
				counter[i] = count + 1
			else:
				counter[i] += 1
		for key,value in sorted(counter.items()):
			print(key," : ",value)
		for i in letters:
			if i not in txt.lower().replace(" ", ""):
				print(i," : not in text file")
except FileNotFoundError : print("File not found, try again!")
