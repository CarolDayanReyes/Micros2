import numpy as np
import matplotlib.pyplot as plt

def calcular_trayectoria(velocidades, d, dt=0.1):
    """
    Calcula la trayectoria del carro dada una lista de velocidades de las ruedas.
    
    :param velocidades: Lista de tuplas [(Vr1, Vl1), (Vr2, Vl2), ...]
    :param d: Distancia entre las ruedas
    :param dt: Paso de tiempo entre cada actualización
    :return: Listas con las posiciones x, y y los ángulos
    """
    x, y, alpha = [0], [0], [0]  # Posición y ángulo iniciales
    
    for Vr, Vl in velocidades:
        Vc = (Vr + Vl) / 2
        alpha_p = (Vr - Vl) / (2 * d)
        
        nuevo_x = x[-1] + Vc * np.cos(alpha[-1]) * dt
        nuevo_y = y[-1] + Vc * np.sin(alpha[-1]) * dt
        nuevo_alpha = alpha[-1] + alpha_p * dt
        
        x.append(nuevo_x)
        y.append(nuevo_y)
        alpha.append(nuevo_alpha)
    
    return x, y, alpha

# Parámetros
d = 0.5  # Distancia entre ruedas
dt = 0.1  # Paso de tiempo

# Lista de velocidades (ejemplo)
velocidades = [(1, 1), (2, 1), (2, 0), (1, -1), (0, -2)]

# Calcular la trayectoria
x, y, alpha = calcular_trayectoria(velocidades, d, dt)

# Graficar
plt.figure(figsize=(6, 6))
plt.plot(x, y, marker='o', linestyle='-')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Trayectoria del carro")
plt.grid()
plt.show()
