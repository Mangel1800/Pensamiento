# Tarea 8: Montecarlo

# Montecarlo usado en ahorro para el retiro
# Se simulan 1,000 futuros posibles de un ahorro.
# Cada año el rendimiento se sortea al azar (promedio 8%, puede variar +-12%).

import random
import matplotlib.pyplot as plt

random.seed(42)      # para que siempre salgan los mismos numeros

# Parametros
ahorro_inicial = 10000     # pesos con los que empiezas
aportacion = 24000         # lo que metes cada año (2,000 al mes)
anios = 43                 # de los 22 a los 65 años
simulaciones = 1000        # cuantos futuros vamos a simular

# Simulacion de Montecarlo
resultados = []

for i in range(simulaciones):                       # cada futuro
    saldo = ahorro_inicial
    for anio in range(anios):                       # cada año de ese futuro
        rendimiento = random.gauss(0.08, 0.12)      # rendimiento al azar: promedio 8%, desviacion 12%
        saldo = saldo * (1 + rendimiento) + aportacion   # crece y se mete la aportacion
    resultados.append(saldo)                        # se guarda como termino ese futuro

# Resultados
resultados.sort()                                   # de menor a mayor

print(f'Futuros simulados: {len(resultados)}')
print(f'Peor caso:  ${resultados[0]:,.0f}')
print(f'Promedio:   ${sum(resultados) / len(resultados):,.0f}')
print(f'Mejor caso: ${resultados[-1]:,.0f}')

# Grafica: cuantos futuros terminaron con cada cantidad de dinero
plt.figure(figsize=(10, 5))
plt.hist(resultados, bins=50, color='skyblue', edgecolor='black')
plt.title('Saldo final en 1,000 futuros')
plt.xlabel('Saldo a los 65 años (pesos)')
plt.ylabel('Frecuencia')
plt.show()
