import pandas as pd

df = pd.read_csv('precinct-data.csv', dtype={'GEOID20':str})
df.groupby(['District', 'From']).agg({'T_20_CENS_Total': sum,'E_24_PRES_Dem':sum, 'E_24_PRES_Rep':sum, 'E_24_PRES_Total': sum, 'E_20_PRES_Dem':sum, 'E_20_PRES_Rep':sum, 'E_20_PRES_Total': sum}).to_csv('Export.csv')

print('Done')
