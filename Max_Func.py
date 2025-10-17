import numpy as np
import matplotlib.pyplot as plt

# Definir la función
def f(x):
    return x**2 - 3*x + 4

# Definir el intervalo cerrado [x_min, x_max]
x_min = 0  # Límite inferior del intervalo
x_max = 3  # Límite superior del intervalo

# Evaluar la función en los extremos del intervalo
f_min = f(x_min)
f_max = f(x_max)

# Encontrar el máximo en el intervalo
if f_min > f_max:
    x_maximo = x_min
    f_maximo = f_min
else:
    x_maximo = x_max
    f_maximo = f_max

print(f"El máximo en el intervalo [{x_min}, {x_max}] está en x = {x_maximo}, f(x) = {f_maximo}")

# Generar puntos para graficar
x = np.linspace(x_min - 0.5, x_max + 0.5, 100)
y = f(x)

# Graficar la función y el máximo
plt.plot(x, y, label='f(x) = x^2 - 3x + 4')
plt.scatter([x_maximo], [f_maximo], color='red', label=f'Máximo en x={x_maximo}')
plt.axvline(x_min, color='gray', linestyle='--', label='Límites del intervalo')
plt.axvline(x_max, color='gray', linestyle='--')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Máximo de la función en el intervalo cerrado')
plt.legend()
plt.grid(True)
plt.show()
