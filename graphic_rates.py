import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mtick
data = pd.read_excel('datos_graficos.xlsx', sheet_name="tasas", decimal=',')
variables = data.iloc[:, 0]
df = data.iloc[:, 1:].T
df.columns = variables
df.index = df.index.astype(int)
df = df.apply(pd.to_numeric, errors='coerce')

# 🎨 Custom color palette (add more if needed)
colors = ['#8475e0', '#f89c49', '#f51e92', '#77ccc7', '#F6C85F', '#6B5B95']

plt.figure(figsize=(10, 6))

for i, col in enumerate(df.columns):
    plt.plot(df.index, df[col], label=col, color=colors[i % len(colors)], linewidth=2)
    
    # subtle value labels
    for x, y in zip(df.index, df[col]):
        plt.text(x, y, f'{y*100:.3f}%', fontsize=7, ha='center', va='bottom', alpha=0.7)

# Labels & title
plt.xlabel('Año', fontsize=11)
plt.ylabel('Tasa de Crecimiento Inercial', fontsize=11)
plt.title('Crecimiento de Variables', fontsize=13, weight='bold')

# Minimalist grid (only horizontal)
plt.grid(axis='y', linestyle='--', linewidth=0.6, alpha=0.5)

# Remove top/right borders
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Keep clean ticks
plt.xticks(df.index, fontsize=9)
plt.yticks(fontsize=9)

# Clean legend
plt.legend(frameon=False, fontsize=9)

plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(1))
plt.tight_layout()
plt.show()