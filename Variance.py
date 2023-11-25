#To know the variance of the sales 
import pandas as pd
import matplotlib.pyplot as plt

csv_file_path = '/Users/joaquinhirokicampos/Desktop/BJJ/Datos Negocios.csv'

df = pd.read_csv(csv_file_path)

variance_sales_by_group = df.groupby('Carrera')['Gasto total'].var()

plt.bar(variance_sales_by_group.index, variance_sales_by_group.values)
plt.xlabel('Carrera')
plt.ylabel('Sales Variance')
plt.title('Frequency Diagram of Sales Variance by Major')
plt.xticks(rotation=45, ha='right')  
plt.show()
