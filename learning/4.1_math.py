# arithmetic funcions
# let's define a few variables

a_0 = 1
a_1 = 1
a_2 = 2
a_3 = 3
a_4 = 5

# augmented assignment operators = <ovar> = <ivar1> <operator> <number> --> <ivar> {operator}= <num>

# addition
a1 = a_0 + a_1 # outputs 2
a2 = a_0 + 1 # outputs 2
a_0 += 1 # augmented assignment operator

a_0 = 1
a_1 = 1
a_2 = 2
a_3 = 3
a_4 = 5

# subtraction
b1 = a_0 - a_1 # outputs 0
b2 = a_0 - 1 # outputs 0
a_0 -= 1 # augmented assignment operator

a_0 = 1
a_1 = 1
a_2 = 2
a_3 = 3
a_4 = 5

# multiplication
c1 = a_0 * a_2 # outputs 2
c2 = a_0 * 2 # outputs 2
a_0 *= 2 # augmented assignment operator

a_0 = 1
a_1 = 1
a_2 = 2
a_3 = 3
a_4 = 5

# division
d1 = a_2 / a_0 # outputs 2
d2 = a_2 / 1 # outputs 2
a_2 /= 1 # augmented assignment operator

a_0 = 1
a_1 = 1
a_2 = 2
a_3 = 3
a_4 = 5

# exponentiation
e1 = a_2 ** a_2 # outputs 4
e2 = a_2 ** 2 # outputs 4

a_0 = 1
a_1 = 1
a_2 = 2
a_3 = 3
a_4 = 5

# modulo --> outputs the remainder upon division
f1 = a_3 % a_2 # outputs 1
f2 = a_4 % 2 # outputs 1
a_4 %= 2

print(a1, a2)
print(b1, b2)
print(c1, c2)
print(d1, d2)
print(e1, e2)
print(f1, f2)