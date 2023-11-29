print('Welcome to Taxicab Conundrum')
x = 0 + 0j
s = input("Enter directions: ")
for i in s:
    if i.lower() == 'n':
        x += 1j
    elif i.lower() == 's':
        x -= 1j
    elif i.lower() == 'e':
        x += 1
    elif i.lower() == 'w':
        x -= 1
    elif i.lower() == 'r':
        x = 0 + 0j
# i, r = x.imag, x.real
# i, r = int(i),int(r)
print(len(s))
print(x)
d = int(abs(x))
print('The Distance from the initial is position is:', d)
