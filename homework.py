import pandas as pd

df = pd.read_csv('data/itresume-users-pandas.csv', encoding='1251')

df['something else here :)'] = df['something else here :)'].str.split(';')
df[['id', 'username', 'date_joined']] = df['something else here :)'].tolist()
df.drop('something else here :)', axis=1, inplace=True)
df = df.drop(0)
df = df.set_index(df.index - df.index[0])
df.replace('', 'NaN', inplace=True)

params = {
    'Имена столбцов': list(df.columns),
    'Размер': len(df.index)*len(df.columns),
    'Форма': df.shape
}


print(params)