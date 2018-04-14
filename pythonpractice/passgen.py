import string
from random import *


chars = string.ascii_letters + string.punctuation + string.digits
password = ("".join(choice(chars) for x in range(randint(64, 64))))
print (password)
