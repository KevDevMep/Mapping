import pandas as pd

def firstFive(df:pd.Dataframe, C: dict):
    index = df.index
    df['County_Name'] = ''
    for i in index:
        df.loc[i, 'GEOID20'] = df['GEOID20'][i][0:5]
        df.loc[i, 'County_Name'] = C[df['GEOID20'][i]]

def countyDict(df: pd.Dataframe):
    C = {}
    index = df.index
    for i in index:
        C[df['GEOID20'][i]] = df['Name'][i]
    return C

def splits(df: pd.Dataframe):
    counter = {}
    split = set()
    index = df.index
    for i in index:
        counter[df['County_Name'][i]] = counter.get(df['County_Name'][i], 0) + 1
    for j in counter.keys():
        if counter[j] > 1:
            split.add(j)

    return split

def update(df: pd.Dataframe, split: set):
    index = df.index
    for i in index:
        if df['County_Name'][i] in split:
            df.loc[i, 'County_Name'] = (df['County_Name'][i] + " (pt.)")

counties_df = pd.read_csv('county-data.csv', dtype={'GEOID20':str})
C = countyDict(counties_df)
df = pd.read_csv('precinct-data.csv', dtype={'GEOID20':str})
df = df[(df['District'] != 0)].dropna()
firstFive(df, C)
# print(df)

# df.groupby(['District', 'County_Name']).agg({'X_24_New_Jersey_President_2024_D':sum, 'X_24_New_Jersey_President_2024_R':sum, 'X_24_New_Jersey_President_2024_Tot': sum, 'E_20_PRES_Dem':sum, 'E_20_PRES_Rep':sum, 'E_20_PRES_Total': sum}).to_csv('Export.csv')
df.groupby(['District', 'County_Name']).agg({'E_24_PRES_Dem':sum, 'E_24_PRES_Rep':sum, 'E_24_PRES_Total': sum, 'E_20_PRES_Dem':sum, 'E_20_PRES_Rep':sum, 'E_20_PRES_Total': sum}).to_csv('Export.csv')

df_B = pd.read_csv('Export.csv')
split = splits(df_B)
update(df_B, split)
total = pd.Series([0, 'Grand Total', df['E_24_PRES_Dem'].sum(), df['E_24_PRES_Rep'].sum(), df['E_24_PRES_Total'].sum(), df['E_20_PRES_Dem'].sum(), df['E_20_PRES_Rep'].sum(), df['E_20_PRES_Total'].sum()], index=['District', 'County_Name', 'E_24_PRES_Dem', 'E_24_PRES_Rep', 'E_24_PRES_Total', 'E_20_PRES_Dem', 'E_20_PRES_Rep', 'E_20_PRES_Total'])
df_B = pd.concat([df_B, total.to_frame().T], ignore_index=True)
df_B.to_csv('Export_Fin.csv')

print('Done')
