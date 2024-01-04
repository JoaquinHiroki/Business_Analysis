#Joaquín Hiroki Campos Kishi, Baxter Technical/Business Case


import pandas as pd 
from datetime import datetime, timedelta 

users_list_cvs = '/Users/joaquinhirokicampos/Desktop/Baxter Interview/UsersList.csv'
non_active_cvs = '/Users/joaquinhirokicampos/Desktop/Baxter Interview/NotActiveUsers.csv'

df = pd.read_csv(users_list_cvs)
print("Column Names:", df.columns)
df['Last Login'] = pd.to_datetime(df['Last Login'], format = '%m/%d/%Y %H:%M', errors = 'coerce')
df['UserCreatedAt'] = pd.to_datetime(df['UserCreatedAt'], format = '%Y-%m-%d %H:%M:%S', errors = 'coerce')
print("DataFrame Preview:")
print(df.head())

revoke_date = datetime.now() - timedelta(days = 120)

inactive_users = df[df['Last Login'] < revoke_date]
print(inactive_users[['Username', 'Last Login']])

inactive_users.to_csv(non_active_cvs, index = False)



