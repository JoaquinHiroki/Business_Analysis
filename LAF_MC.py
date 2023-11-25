#Most consumed product by LAF the major that buys the most at the business selected
import pandas as pd
import matplotlib.pyplot as plt

csv_file_path = '/Users/joaquinhirokicampos/Desktop/BJJ/Datos Negocios.csv'

df = pd.read_csv(csv_file_path)

filtered_df = df[df['Carrera'] == 'LAF']

producto1_counts = filtered_df['Producto 1'].value_counts()

plt.bar(producto1_counts.index, producto1_counts.values)
plt.xlabel('Producto 1')
plt.ylabel('Times')
plt.title('Most consumed product by LAF')
plt.xticks(rotation=45, ha='right')  
plt.show()

