#To know the mean of the sales 
import pandas as pd
import matplotlib.pyplot as plt

csv_file_path = '/Users/joaquinhirokicampos/Desktop/BJJ/Datos Negocios.csv'

df = pd.read_csv(csv_file_path)

mean_sales_by_group = df.groupby('Carrera')['Gasto total'].mean()

plt.bar(mean_sales_by_group.index, mean_sales_by_group.values)
plt.xlabel('Carrera')
plt.ylabel('Mean Sales')
plt.title('Frequency Diagram of Mean Sales by Major')
plt.xticks(rotation=45, ha='right')  
plt.show()
