# Insira o valor de comprimento de onda e receba o valor de energia dessa onde em eV


# Constantes
h = 6.626 * 10**(-34)
c = 3 * 10**8
# Input
lamb = 700 * 10**(-9)
# Contas
f = c / lamb
E = h * f
ev = E / (1.6 * 10**(-19))
# Resultado
print(round(ev, 4), 'eV')

# Dê a energia e receba o comprimento de onda
print()

# Input
ev = 0.0012
# Contas
E = ev * (1.6 * 10**(-19))
lamb = h * c / E
# Resultado

print(lamb * 10**9, 'nm')

# Insira a energia e receba a frequência
print()

# Input
ev = 0.0012
# Contas
E = ev * (1.6 * 10**(-19))
f = E / h
# Resultado

print(f, 'Hz')