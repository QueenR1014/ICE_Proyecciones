import pandas as pd
import matplotlib.pyplot as plt
from graphic_rates import colors
# 1. Leer archivo (ahora SÍ tiene header)
data = pd.read_excel('datos_graficos.xlsx')

# 2. Primera columna = nombres de variables
variables = data.iloc[:, 0]

# 3. El resto son datos → transponer
df = data.iloc[:, 1:].T

# 4. Asignar nombres de columnas (variables)
df.columns = variables

# 5. Usar los años como eje X
df.index = df.index.astype(int)  # por si están como string

# 6. Convertir a numérico
df = df.apply(pd.to_numeric, errors='coerce')

# 7. Graficar
plt.figure()

for i, col in enumerate(df.columns):
    plt.plot(df.index, df[col], label=col, color=colors[i % len(colors)], linewidth=2)

plt.xlabel('Años')
plt.ylabel('PIB real')
plt.title('PIB real anual')
plt.legend()

plt.show()


df_last10 = df.tail(8)
plt.figure()

for i, col in enumerate(df_last10.columns):
    plt.plot(df_last10.index, df_last10[col], label=col, color=colors[i % len(colors)], linewidth=2)

plt.xlabel('Años')
plt.ylabel('PIB real')
plt.title('Últimos 8 años')
plt.legend()

plt.show()