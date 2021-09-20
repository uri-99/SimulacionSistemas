
speeds = [0.005, 0.01, 0.015, 0.02]
eks = [] ##input, xi
pressures = [0.06432478245847889, 0.25819076499992144, 0.5796720828451926, 1.0167769649687661] #observable, yi
datos = []

for i in range(4):
    aux = []
    aux.append((speeds[i]**2)/2)
    aux.append(pressures[i])#*0.0216)
    datos.append(aux)

print(datos)

#PV = nRT

def Ajuste(m, x, c=0):
    return m*x + c



def Error(m,c=0):
    sum = 0
    for dato in datos:
        sum += (dato[1] - Ajuste(m, dato[0] ,c))**2
    return sum

min = [999, 0, 0]

for mm in range(10000):
    if mm%10000 == 0:
        print(mm)
    mmm = mm/10000 + 5103
    e = Error(mmm)
    if e < min[0]:
        min[0] = e
        min[1] = mm

print(min)

