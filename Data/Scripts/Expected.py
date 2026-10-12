import pandas as pd

def expected(df: pd.Dataframe):
    index = df.index
    df['Expected'] = 0.0
    for i in index:
        df.loc[i, 'Expected'] = max(0, min(1, 0.5 + 5 * (df['Margin'][i])))
while 1:
    fileName = input("Filename: ")
    if fileName == '0':
        break
    df = pd.read_csv(fileName)
    expected(df)
    df.groupby('State').agg({'Expected':sum}).to_csv('Export.csv')
    print('Export')

print('Done')
