pi = 22/7
with open('pi_digits.txt','w') as file:
    file.write(str(pi))
with open('pi_digits.txt') as file:
    lines = file.read()
print(lines[:4])