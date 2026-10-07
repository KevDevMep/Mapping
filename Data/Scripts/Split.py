import pandas as pd

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

df = pd.read_csv('Export.csv')
split = splits(df)
update(df, split)
df.to_csv('Export_Fin.csv')
print('Done')

