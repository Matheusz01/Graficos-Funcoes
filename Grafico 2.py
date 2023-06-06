import matplotlib.pyplot as plt
import numpy as np

# Define a função para o volume de água no tanque
def V(t):
    return 50 - 2*t**2

# Cria um array de valores de t (de 0 a 360 minutos, com incremento de 1 minuto)
t = np.arange(0, 361, 1)

# Calcula o volume de água correspondente a cada valor de t
volume = V(t)

# Cria o gráfico
plt.plot(t/60, volume)  # Mantém o volume na orientação correta

# Inverte o eixo y
plt.gca().invert_yaxis()

# Adiciona rótulos aos eixos
plt.xlabel('Tempo (horas)')
plt.ylabel('Volume de água (m³)')

# Adiciona um título ao gráfico
plt.title('Esvaziamento do tanque de água da chuva')

# Localiza os pontos de interesse
t_esvaziamento = np.where(volume <= 0)[0][0]
t_interesse = [0, t_esvaziamento]
volume_interesse = [V(0), V(t_esvaziamento)]

# Plota os pontos de interesse no gráfico
plt.scatter(np.array(t_interesse)/60, volume_interesse, color='red', label='Pontos de interesse')

# Adiciona uma legenda
plt.legend()

# Exibe o gráfico
plt.show()

# Calcula o tempo necessário para esvaziar o tanque em horas
tempo_esvaziamento = t_esvaziamento / 60

print(f"O tempo necessário para esvaziar o tanque é de aproximadamente {tempo_esvaziamento:.2f} horas.")
