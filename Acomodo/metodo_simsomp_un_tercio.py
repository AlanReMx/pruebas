# crear contenido del archivo metodo_simsomp_un_tercio.py
def metodo_simsomp_un_tercio(f, a, b, tol, max_iter=100):
    """
    Método de Simpson 1/3 para la integración numérica.
    
    Parámetros:
        f: función a integrar
        a: límite inferior de integración
        b: límite superior de integración
        tol: tolerancia para el error
        max_iter: número máximo de iteraciones (opcional)
    Retorna:
        Aproximación de la integral definida de f en [a, b]
    """
    n = 2  # Simpson 1/3 requiere al menos 2 subintervalos (n par)
    h = (b - a) / n
    integral_old = 0.0

    for _ in range(max_iter):
        x = [a + i * h for i in range(n + 1)]
        y = [f(xi) for xi in x]
        integral = y[0] + y[-1]
        integral += 4 * sum(y[1:-1:2])
        integral += 2 * sum(y[2:-2:2])
        integral *= h / 3

        if abs(integral - integral_old) < tol:
            return integral

        integral_old = integral
        n *= 2
        h = (b - a) / n

    return integral  # Devuelve la última aproximación si no se alcanza la tolerancia