m = 10**(-3)
a = 10 * m
b = 300 * m
h = 0.05 * m
g = 9.8
h_descida = 0.01 * m
dens = 7.8 #g/cm³
vol = a * b * h
vol_cm = vol * 10**6
print(vol_cm, 'cm³')
massa = dens * vol_cm
massa_kg = massa * m
print(massa, 'g')
tensao = 72 * m
area = 2*a*h_descida + 2*b*h_descida
wsup = area * tensao
print('Energia para alterar área superficial:',round(wsup * 10**6,5), 'micro Joule')

wdes = massa_kg * g * h_descida
print('Energia potencial:',round(wdes * 10**6,5), 'micro Joule')
print()
if wsup > wdes:
    print('A energia para alterar a superfície da água é maior que a energia potencial ganhada na descida, devido a isso o material se mantém na superfície!')
else:
    print('AFUNDOUUUU!')
print()
