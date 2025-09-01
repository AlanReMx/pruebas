import cmath  # Para números complejos
import math

def resolver_cubica(a, b, c, d):
    if a == 0:
        raise ValueError("No es una ecuación cúbica (a no puede ser 0).")
    
    # Cambiamos la forma a: x^3 + px + q = 0 mediante cambio de variable
    f = ((3 * c / a) - ((b ** 2) / (a ** 2))) / 3
    g = ((2 * b ** 3) / (a ** 3) - (9 * b * c) / (a ** 2) + (27 * d / a)) / 27
    h = (g ** 2) / 4 + (f ** 3) / 27

    # Comprobamos el discriminante h
    if h > 0:
        # Una raíz real y dos complejas
        R = -(g / 2) + cmath.sqrt(h)
        S = R ** (1 / 3)

        T = -(g / 2) - cmath.sqrt(h)
        U = T ** (1 / 3)

        x1 = S + U - (b / (3 * a))
        x2 = -(S + U) / 2 - (b / (3 * a)) + (S - U) * cmath.sqrt(3) * 1j / 2
        x3 = -(S + U) / 2 - (b / (3 * a)) - (S - U) * cmath.sqrt(3) * 1j / 2
    elif h == 0:
        # Todas las raíces reales, al menos dos son iguales
        S = (-(g / 2)) ** (1 / 3)
        x1 = 2 * S - (b / (3 * a))
        x2 = x3 = -S - (b / (3 * a))
    else:
        # Tres raíces reales y desiguales (caso de Cardano real)
        i = math.sqrt(((g ** 2) / 4) - h)
        j = i ** (1 / 3)
        k = math.acos(-(g / (2 * i)))
        L = -j
        M = math.cos(k / 3)
        N = math.sqrt(3) * math.sin(k / 3)
        P = -(b / (3 * a))
        x1 = 2 * j * math.cos(k / 3) - (b / (3 * a))
        x2 = L * (M + N) + P
        x3 = L * (M - N) + P

    return x1, x2, x3


# Ejemplo de uso
a, b, c, d = 1, -6, 11, -6  # x³ - 6x² + 11x - 6 = 0 → Raíces: 1, 2, 3
raices = resolver_cubica(a, b, c, d)
print("Raíces:", raices)
