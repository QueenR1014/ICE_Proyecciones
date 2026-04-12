import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 🔥 clave: decimal=","
data = pd.read_excel('datos_graficos.xlsx', sheet_name="tasas", decimal=',')

# 🔥 limpiar nombres de columnas
data.columns = data.columns.str.strip()

print(data.columns)  # para verificar

df = data.set_index('Sector')
# 1. Usar "Sector" como índice
df = data.set_index('Sector')

# 2. Transponer (AHORA sí tiene sentido)
df = df.T

# 3. Asegurar que el índice (años) sea numérico
df.index = df.index.astype(int)

print(df.shape)      # debería ser (11, 4)
print(df.columns)    # las 4 variables

# --- gráfica ---
df = df.tail(10)

x = np.arange(len(df.index))
width = 0.2
n = len(df.columns)

plt.figure()

for i, col in enumerate(df.columns):
    plt.bar(x + (i - n/2)*width + width/2, df[col], width=width, label=col)

plt.xticks(x, df.index, rotation=45)

plt.xlabel("Año")
plt.ylabel("Tasa de Crecimiento")
plt.title("Tasas de Crecimiento del PIB por escenario y tipo")
plt.axhline(0)  # 🔥 muy útil para tasas

plt.legend()
plt.tight_layout()
plt.show()