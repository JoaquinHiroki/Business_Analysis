#Major that buys the most in the business selected 
import pandas as pd
import matplotlib.pyplot as plt

csv_file_path = '/Users/joaquinhirokicampos/Desktop/BJJ/Datos Negocios.csv'

df = pd.read_csv(csv_file_path)

carrera_counts = df['Carrera'].value_counts()

plt.bar(carrera_counts.index, carrera_counts.values)
plt.xlabel('Major')
plt.ylabel('Times')
plt.title('Most repeated major')
plt.xticks(rotation=45, ha='right')  
plt.show()
