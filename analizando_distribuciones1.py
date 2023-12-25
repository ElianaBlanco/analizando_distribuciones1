import pandas as pd
import matplotlib.pyplot as plt


# Graficar la distribución de edades con un histograma
plt.figure(figsize=(8, 5))
plt.hist(df['age'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribución de Edades')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()

# Histogramas agrupados por características
features = ['anaemia', 'diabetes', 'smoking', 'DEATH_EVENT']
gender_mapping = {0: 'Mujer', 1: 'Hombre'}

for feature in features:
    plt.figure(figsize=(8, 5))
    for gender in df['sex'].unique():
        filtered_data = df[df['sex'] == gender][feature]
        bins = filtered_data.nunique()
        plt.hist(filtered_data, bins=bins, alpha=0.5, label=gender_mapping[gender], align='edge')

    plt.title(f'Histograma de {feature} por género')
    plt.xlabel(feature)
    plt.ylabel('Frecuencia')
    plt.legend()
    plt.grid(True)
    plt.show()
