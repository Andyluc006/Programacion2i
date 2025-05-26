def computepay(horas, tarifa):
    if horas > 40:
        extras = horas - 40
        salario = 40 * tarifa + extras * (tarifa * 1.5)
    else:
        salario = horas * tarifa
    return salario
horas = 45
tarifa = 10

salario = computepay(horas, tarifa)

print("Salario:", salario)
    