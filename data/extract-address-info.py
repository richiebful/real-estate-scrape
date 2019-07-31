import pandas as pd
import numpy as np

df_addresspts = pd.read_csv('Allegheny_County_Address_Points.csv', usecols=['ADDR_NUM', 'ST_NAME', 'MUNICIPALITY'], dtype={'ADDR_NUM': str, 'ST_NAME':str, 'MUNICIPALITY':str})
slice_addresslookup = df_addresspts[['ADDR_NUM', 'ST_NAME', 'MUNICIPALITY']]

df_municipality = pd.read_csv('municipality_lookup.csv',
                              usecols=[
                                  'AddressListDescription', 'PortalMunicipalityCode', 'PortalMunicipalityDescription'],
                              dtype={
                                  'AddressListDescription': str, 'PortalMunicipalityCode': str, 'PortalMunicipalityDescription': str})
df_addresspts = df_addresspts.merge(
    df_municipality, how='left', left_on='MUNICIPALITY', right_on='AddressListDescription')
df_addresspts.to_parquet('address_points.parquet', compression='snappy')