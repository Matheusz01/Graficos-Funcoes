import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return -t**2 + 30*t - 216

# Intervalo de t para o gráfico
t = np.linspace(12, 18, 100)

# Valores correspondentes de f(t)
y = f(t)

# Encontrando o ponto máximo
max_index = np.argmax(y)
t_max = t[max_index]
y_max = y[max_index]

# Plotando o gráfico
plt.plot(t, y, label='f(t)=-t²+30t-216')
plt.scatter(t_max, y_max, color='red', label=f'Máximo ({t_max:.2f}, {y_max:.2f})')
plt.xlabel('Hora (t)')
plt.ylabel('Número de Ocorrências (f)')
plt.legend()
plt.title('Gráfico do Número de Ocorrências')
plt.grid(True)
plt.show()
