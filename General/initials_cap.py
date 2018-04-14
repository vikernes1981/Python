
def initials(text):
    start = text.split()
    char = []
    init = []
    for i in range(len(start)):
        char.append(start[i].split())
    for c in range(len(char)):
        if  char[c][0][0].isalpha():
            init.append(char[c][0][0].upper())
    init = str(init)
    init = init.replace(',','')
    init = init.replace("'", "")
    init = init.replace('[', '')
    init = init.replace(']', '')
    init = init.replace(" ", ". ")
    init = init + "."
    return init
text = "Να κατασκευάσετε συνάρτηση initials(text) που δέχεται _ ως είσοδο 0 ένα κείμενο =    και επιστρέφει το κείμενο με το αρχικό μόνο σύμβολο κάθε λέξης του έχοντας μετατραπεί σε κεφαλαίο, π.χ. αν text = Καλημέρα σας κυρίες και κύριοι, επιστρέφει:"

print(initials(text))
