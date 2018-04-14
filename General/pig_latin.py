pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha(): # dld True
    #.lower ta kanei ola mikra
    word = original.lower()
    #pernei to prwto gramma ths lekshs
    first = word[0]
    #prosthetei leksh syn to prwto gramma syn to 'ay'
    new_word = word + first + pyg
    #allagh lsekshs( xwris to prwto gramma)
    new_word = new_word[1:len(new_word)]
    print new_word
else:
    print 'empty'