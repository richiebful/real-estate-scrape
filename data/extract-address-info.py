import pandas as pd

df_addresspts = pd.read_csv('Allegheny_County_Address_Points.csv')
slice_addresslookup = df_addresspts[['ADDR_NUM','ST_NAME', 'MUNICIPALITY']]

munilist = slice_addresslookup['MUNICIPALITY'].unique().tolist()
print('\n'.join(munilist))