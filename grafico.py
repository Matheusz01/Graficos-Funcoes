import matplotlib.pyplot as plt
import numpy as np

# Define a função para o número de infectados
def f(t):
    return -2*t**2 + 120*t

# Cria um array de valores de t (60 primeiros dias)
t = np.linspace(0, 60, 100)

# Calcula o número de infectados correspondente a cada dia
infectados = f(t)

# Cria o gráfico
plt.plot(t, infectados)

# Encontra os pontos de interesse (t1 e t2)
t1 = np.roots([-2, 120, -1600])[0]
t2 = np.roots([-2, 120, -1600])[1]

# Calcula os valores de infectados nos pontos de interesse
f_t1 = f(t1)
f_t2 = f(t2)

# Plota os pontos de interesse no gráfico
plt.scatter(t1, f_t1, color='red', label='t1')
plt.scatter(t2, f_t2, color='blue', label='t2')

# Adiciona rótulos aos eixos
plt.xlabel('Dias')
plt.ylabel('Número de infectados')

# Adiciona um título ao gráfico
plt.title('Número de infectados ao longo dos dias')

# Adiciona uma legenda
plt.legend()

# Exibe o gráfico
plt.show()
