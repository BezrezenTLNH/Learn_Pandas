import pandas as pd

df = pd.read_csv('data/data.csv', encoding='1251')

#  head - give to us first (x=5) rows
#  tail - the same but from end
#  set_option - standart options of output
#  describe_option
pd.set_option('display.max_columns', 40)

#  dtypes - check type of output
pd.set_option('display.float_format', '{:.2f}'.format)

#  show the qty of rows and columns
# print(df.shape)


#  index - show the index
#  columns - show the columns
# print(df.index)
# print(df.columns)


#  to show only intresting columns we can put their names into dataframe
our_cols = ['DR_Dat', 'DR_Tim', 'DR_NChk', 'DR_NDoc', 'DR_Apt',
            'DR_NDrugs', 'DR_Kol', 'DR_CZak', 'DR_CRoz', 'DR_SDisc',
            'DR_TPay', 'DR_CDrugs', 'DR_NDrugs', 'DR_Suppl',
            'DR_CDisc', 'DR_BCDisc', 'DR_TabEmpl', 'DR_VZak', 'DR_Pos']
# print(df[['DR_Dat', 'DR_Tim']])
df = df[our_cols]


#  rename the columns
df.columns = ['dt', 'c_time', 'nchk', 'ndoc', 'apt', 'drug_id', 'kol', 'zak', 'roz', 's_disc',
              'pay_type', 'cdrugs', 'ndrugs', 'suppl', 'cdisc', 'bcdisc', 'tablempl', 'vzak', 'pos']

#  we can add dtype after any data that has taken from dataframe
# print(df['bcdisc'].dtype)

#  and we can change the type using .astype()
df['bcdisc'] = df['bcdisc'].astype('str').replace('\.0', '', regex=True)
df['cdisc'] = df['cdisc'].astype('str').replace('\.0', '', regex=True)

#  we can change the dates format to datetime using to_datetime
#  we can take info using .dt.FORMAT (year, day_of_week, day_of_year, etc...)
#  adn using strftime('%d.%m.%Y')
pd.to_datetime(df['dt']).dt.strftime('%d.%m.%Y')

#  change type
df['vzak'].unique()
df['vzak'] = df['vzak'].astype('str').replace('1', 'Usual').replace('2', 'Internet-shop')

#  find all none using isna()
df.isna().any()

#  change all none to some using fillna(), all none -> 0
df.fillna('0')

#  if data is empty and must be filled by mathematical operations -> interpolate(method='cubic')
#  if we need to delete all empty or none .dropna()
# print(df.shape)
# print(df.dropna(axis=1).shape)


#  check info
df.info()

#  check all statistics
df.describe()

#  check value counts
df['pay_type'].value_counts()
#  you can also check columns by their names:
df.pay_type.value_counts()

#  if we want to see the results in % we should add(normalize-True)