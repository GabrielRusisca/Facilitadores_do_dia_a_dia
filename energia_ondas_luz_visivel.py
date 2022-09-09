print()
print()
# Constantes
planck = 6.626 * 10**(-34)
velocidade_da_luz = 3 * 10**8
# Comprimento de onda dos limites da luz visível
comprimento_de_onda = [400,700]
# cálculos e resultado
for lamb_da in comprimento_de_onda:
    frequencia = velocidade_da_luz / (lamb_da * 10**(-9)) 
    Energia = planck * frequencia
    eV = Energia / (1.6 * 10**(-19))
    print(f'A energia correspondente a onda de {lamb_da} nm é de : {round(eV,2)} eV')


print()
print()