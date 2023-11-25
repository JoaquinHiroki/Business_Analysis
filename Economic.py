#Histogram to know the economic impact of every major in the business selected 
import pandas as pd
import matplotlib.pyplot as plt

csv_file_path = '/Users/joaquinhirokicampos/Desktop/BJJ/Datos Negocios.csv'

df = pd.read_csv(csv_file_path)

carrera_gasto_total_sum = df.groupby('Carrera')['Gasto total'].sum()

plt.bar(carrera_gasto_total_sum.index, carrera_gasto_total_sum.values)
plt.xlabel('Major')
plt.ylabel('Total cost')
plt.title('Total cost by major')
plt.xticks(rotation=45, ha='right')  
plt.show()
