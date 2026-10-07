import geopandas as gp

gdf = gp.GeoDataFrame()

def export(type_: str, tag: str):
    match type_:
        case 'GeoJson':
            gdf.to_file(f'{tag}.geojson', use_arrow=True, driver='GeoJson')
        case 'ShapeFile':
            gdf.to_file(f'{tag}.shp', use_arrow=True)
        case 'GeoPackage':
            gdf.to_file(f'{tag}.gpkg', use_arrow=True, driver='GPKG')
        case 'CSV':
            gdf.drop(columns=['geometry']).to_csv(f'{tag}.csv')
        case 'Json':
            gdf.drop(columns=['geometry']).to_json(f'{tag}.json')
        case 'HTML':
            gdf.drop(columns=['geometry']).to_html(f'{tag}.html')
    print(f'Exported {tag}.{type_}')

def minority():
    gdf['Minority'] = ''
    for i in range(len(gdf)):
        if gdf['WhitePct'][i] > .5:
            gdf.loc[i, 'Minority'] = "White"
        elif gdf['HispanicPct'][i] > gdf['WhitePct'][i] and gdf['HispanicPct'][i] > gdf['BlackPct'][i] and gdf['HispanicPct'][i] > gdf['AsianPct'][i] and gdf['HispanicPct'][i] > gdf['NativePct'][i] and gdf['HispanicPct'][i] > gdf['PacificPct'][i]:
            gdf.loc[i, 'Minority'] = "Hispanic"
        elif gdf['BlackPct'][i] > gdf['WhitePct'][i] and gdf['BlackPct'][i] > gdf['AsianPct'][i] and gdf['BlackPct'][i] > gdf['NativePct'][i] and gdf['BlackPct'][i] > gdf['PacificPct'][i]:
            gdf.loc[i, 'Minority'] = "Black"
        elif gdf['AsianPct'][i] > gdf['WhitePct'][i] and gdf['AsianPct'][i] > gdf['NativePct'][i] and gdf['AsianPct'][i] > gdf['PacificPct'][i]:
            gdf.loc[i, 'Minority'] = "Asian"
        elif gdf['NativePct'][i] > gdf['WhitePct'][i] and gdf['NativePct'][i] > gdf['PacificPct'][i]:
            gdf.loc[i, 'Minority'] = "Native"
        elif gdf['PacificPct'][i] > gdf['WhitePct'][i]:
            gdf.loc[i, 'Minority'] = "Pacific"
        else:
            gdf.loc[i, 'Minority'] = "Minority"
