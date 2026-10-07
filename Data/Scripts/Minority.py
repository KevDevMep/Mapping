import pandas as pd

fileName = input("Filename: ")
df = pd.read_csv(fileName).dropna()
print(df)

def minority(df: pd.Dataframe):
    df['Minority'] = ''
    for i in range(len(df)):
        if df['WhitePct'][i] > .5:
            df.loc[i, 'Minority'] = "White"
        elif df['HispanicPct'][i] > df['WhitePct'][i] and df['HispanicPct'][i] > df['BlackPct'][i] and df['HispanicPct'][i] > df['AsianPct'][i] and df['HispanicPct'][i] > df['NativePct'][i] and df['HispanicPct'][i] > df['PacificPct'][i]:
            df.loc[i, 'Minority'] = "Hispanic"
        elif df['BlackPct'][i] > df['WhitePct'][i] and df['BlackPct'][i] > df['AsianPct'][i] and df['BlackPct'][i] > df['NativePct'][i] and df['BlackPct'][i] > df['PacificPct'][i]:
            df.loc[i, 'Minority'] = "Black"
        elif df['AsianPct'][i] > df['WhitePct'][i] and df['AsianPct'][i] > df['NativePct'][i] and df['AsianPct'][i] > df['PacificPct'][i]:
            df.loc[i, 'Minority'] = "Asian"
        elif df['NativePct'][i] > df['WhitePct'][i] and df['NativePct'][i] > df['PacificPct'][i]:
            df.loc[i, 'Minority'] = "Native"
        elif df['PacificPct'][i] > df['WhitePct'][i]:
            df.loc[i, 'Minority'] = "Pacific"
        else:
            df.loc[i, 'Minority'] = "Minority"
    
minority(df)
df.to_csv("Export.csv")
print('Done')
