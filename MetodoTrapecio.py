def f(x):
    # Define aquí la función que quieres integrar
    return x**2  # Ejemplo: f(x) = x^2

def metodo_trapecio(a, b, n):
    h = (b - a) / n
    suma = f(a) + f(b)
    
    for i in range(1, n):
        xi = a + i * h
        suma += 2 * f(xi)
    
    resultado = (h / 2) * suma
    return resultado

# Ejemplo de uso
a = 0  # Límite inferior
b = 1  # Límite superior
n = 10  # Número de trapecios

aproximacion = metodo_trapecio(a, b, n)
print(f"La aproximación de la integral es: {aproximacion}")
