import math

def formula_general(a, b, c):
    # Verificar que a no sea cero (no sería cuadrática)
    if a == 0:
        return "No es una ecuación cuadrática (a no puede ser 0)."
    
    # Calcular el discriminante
    discriminante = b**2 - 4*a*c

    if discriminante > 0:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        return f"Dos soluciones reales: x1 = {x1}, x2 = {x2}"
    elif discriminante == 0:
        x = -b / (2*a)
        return f"Una solución real: x = {x}"
    else:
        real = -b / (2*a)
        imag = math.sqrt(-discriminante) / (2*a)
        return f"Soluciones complejas: x1 = {real}+{imag}i, x2 = {real}-{imag}i"

# Ejemplo de uso
a = 0
b = 4
c = -5

resultado = formula_general(a, b, c)
print(resultado)
