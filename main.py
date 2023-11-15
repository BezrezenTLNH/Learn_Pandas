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

print(df)
