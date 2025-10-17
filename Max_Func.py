import numpy as np
import matplotlib.pyplot as plt

# Definir la función
def f(x):
    return x**2 - 3*x + 4

# Coeficientes de la función cuadrática: f(x) = ax^2 + bx + c
a = 1
b = -3

# Calcular el vértice
x_vertex = -b / (2 * a)
y_vertex = f(x_vertex)

print(f"El vértice de la función está en x = {x_vertex}, f(x) = {y_vertex}")

# Generar puntos para graficar
x = np.linspace(-1, 4, 100)
y = f(x)

# Graficar
plt.plot(x, y, label='f(x) = x^2 - 3x + 4')
plt.scatter([1.5], [1.75], color='red', label='Vértice (1.5, 1.75)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gráfica de la función')
plt.legend()
plt.grid(True)
plt.show()