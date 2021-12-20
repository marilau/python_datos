import pandas as pd

df = pd.read_csv('employee_data.csv')

print(df.head())
#Castear la columna gender a tipo category
df['gender'] = df['gender'].astype('category')

print(df['employment_status'].unique())
df['employment_status'] = df['employment_status'].astype('category')

df['birth_date'] = df['birth_date'].astype('datetime64')

df.rename(columns={'number':'id'}, inplace=True)

#Eliminar solo valores nulos
df.dropna(axis='columns', how='all', inplace=True)

#Eliminar solo valores nulos en fila. En este caso elimina las filas con menos de 2 elementos
df.dropna(axis='index', thresh=2, inplace=True)

print(df.dtypes)
print(df.head())

df.to_csv('data_final.csv')