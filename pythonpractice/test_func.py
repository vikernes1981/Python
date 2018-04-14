def test_func(a, b, c):
	print "This is a test funtion with 3 parameters: %s , %s and %s." % (a, b, c)

print "We give first names:"
test_func(10, 20, 30)

# naming the parameters
a = 'milk'
b = 'cookies'
c = 'honey'

test_func(a, b, c)

# doing math
test_func(48 + 32, 29 * 3, 530 / 8.6)

# What else now?
test_func(a * 3, a + b, c * 2)

# And another try
test_func(len(a), len(b), len(c))

# And another
test_func(len(a[:-1]), len(b[2:4]), len(c[::-1]))

# I'm on fire
test_func(a[:-1], b[1:4], c[::-1])

# ...
test_func(a[::-1], b[::-1], c[::-1])
