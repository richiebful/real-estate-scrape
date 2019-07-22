import pandas as pd

def removeAfterDash(muni: str):
    dash_index = muni.find(' - ')
    if dash_index == -1:
        return muni
    else:
        return muni[:dash_index]

df_addrmuni = pd.read_csv('munilist.csv')
df_portalmuni = pd.read_csv('portalKeyValue.csv')
df_portalmuni = df_portalmuni.drop('OtherKey', axis=1)

df_portalmuni['Clean_PortalMunicipalityDescription'] = df_portalmuni['PortalMunicipalityDescription'].str.upper()
df_portalmuni['Clean_PortalMunicipalityDescription'] = df_portalmuni['Clean_PortalMunicipalityDescription'].apply(removeAfterDash)
df_addrmuni['Clean_AddressListDescription'] = df_addrmuni['AddressListDescription'].str.replace(' TOWNSHIP', '')
df_addrmuni['Clean_AddressListDescription'] = df_addrmuni['Clean_AddressListDescription'].str.replace(' BOROUGH', '')
df_addrmuni['Clean_AddressListDescription'] = df_addrmuni['Clean_AddressListDescription'].str.replace(' TOWNSHIP', '')
print(df_portalmuni.head())
print(df_addrmuni.head())

df_muni = df_addrmuni.merge(df_portalmuni, how='left', left_on='Clean_AddressListDescription', right_on='Clean_PortalMunicipalityDescription')
df_muni = df_muni.drop(['Clean_PortalMunicipalityDescription', 'Clean_AddressListDescription'], axis=1)
df_muni.to_csv("municipality_lookup.csv")