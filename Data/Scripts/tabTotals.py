import pandas as pd

def setCD(dfB: pd.DataFrame):
    index = dfB.index
    for i in index:
        if dfB.loc[i, 'district'] == 0:
            dfB.loc[i, 'CD'] = dfB.loc[i, 'state_po'] + '-AL'
        elif dfB.loc[i, 'district'] < 10:
            dfB.loc[i, 'CD'] = dfB.loc[i, 'state_po'] + '-0' + str(dfB.loc[i, 'district'])
        else:
            dfB.loc[i, 'CD'] = dfB.loc[i, 'state_po'] + '-' + str(dfB.loc[i, 'district'])
    return dfB

df = pd.read_csv('1976-2024-house.tab')
year = input("Year: ")
df = df[(df["year"] == 2024) & (df["writein"]==False)]
df = setCD(df)
df = df[["CD", "party", "candidatevotes"]]
df.dropna().groupby("CD").agg({"candidatevotes":sum}).to_csv("Test.csv")
