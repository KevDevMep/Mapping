import pandas as pd

df = pd.DataFrame()

def party(df: pd.DataFrame, i: int, district: dict):
    if df.loc[i, 'party'] == 'REPUBLICAN':
        district['REPUBLICAN'] = max(district.get('REPUBLICAN', 0), df.loc[i, 'candidatevotes'])
        district['RC'] = df.loc[i, 'candidate']
    elif df.loc[i, 'party'] in ['DEMOCRAT', 'DEMOCRATIC-FARMER-LABOR', 'DEMOCRATIC-NONPARTISAN LEAGUE']:
        district['DEMOCRAT'] = max(district.get('DEMOCRAT', 0), df.loc[i, 'candidatevotes'])
        district['DC'] = df.loc[i, 'candidate']
    else:
        district['OTHER'] = max(district.get('OTHER', 0), df.loc[i, 'candidatevotes'])

def setCD(df_: pd.DataFrame):
    index = df_.index
    for i in index:
        if df_.loc[i, 'district'] == 0:
            df_.loc[i, 'CD'] = df_.loc[i, 'state_po'] + '-AL'
        elif df_.loc[i, 'district'] < 10:
            df_.loc[i, 'CD'] = df_.loc[i, 'state_po'] + '-0' + str(df_.loc[i, 'district'])
        else:
            df_.loc[i, 'CD'] = df_.loc[i, 'state_po'] + '-' + str(df_.loc[i, 'district'])
    return df_

def toForm(tag: str):
    data, district = {}, {}
    index = df.index
    prev = df.loc[index[0], 'CD']
    for i in index:
        if df.loc[i, 'CD'] != prev:
            if district.get('REPUBLICAN', 0) == 0:
                district['REPUBLICAN'] = 0
            if district.get('DEMOCRAT', 0) == 0:
                district['DEMOCRAT'] = 0
            data[prev] = district
            prev = df.loc[i, 'CD']
            district = {}
            party(df, i, district)
        else:
            party(df, i, district)
    data[prev] = district

    dataDF = pd.DataFrame(data)
    dataDF.transpose().to_csv(f'{tag}.csv')

def toFormNY(tag: str):
    ny = df[df['state_po'] == 'NY']
    data, district = {}, {}
    index = ny.index
    prev = ny.loc[index[0], 'CD']
    for i in index:
        if ny.loc[i, 'CD'] != prev:
            data[prev] = district
            prev = ny.loc[i, 'CD']
            district = {}
            district[ny.loc[i, 'candidate']] = ny.loc[i, 'candidatevotes']
        else:
            district[ny.loc[i, 'candidate']] = ny.loc[i, 'candidatevotes'] + district.get(ny.loc[i, 'candidate'], 0)
    data[prev] = district

    dataDF = pd.DataFrame(data)
    dataDF.to_csv(f'{tag}_NY.csv')

def setUp(df_: pd.DataFrame, year: int):
    df_ = df_[(df_['year'] == year) & (df_['state_po'] != 'DC')]
    df_ = setCD(df_)
    df_ = df_[['state_po', 'CD', 'candidate', 'party', 'candidatevotes']]
    df_ = df_.dropna()
    return df_
