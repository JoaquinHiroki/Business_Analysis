#Box plot of the sales based on the Total cost column
import pandas as pd
import matplotlib.pyplot as plt

csv_file_path = '/Users/joaquinhirokicampos/Desktop/BJJ/Datos Negocios.csv'

df = pd.read_csv(csv_file_path)

plt.boxplot(df['Gasto total'])
plt.xlabel('Sales')
plt.ylabel('Values')
plt.title('Box Plot of the sales')
plt.show()

