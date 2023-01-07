from sqlalchemy import create_engine
import geopandas as gpd
import pandas as pd


user = "postgres"
password = "testtest"
host = "localhost"
port = 5432
database = "postgres"
 
conn = f"postgresql://{user}:{password}@{host}:{port}/{database}"
engine = create_engine(conn)
 

gdf = gpd.read_file("test_shapefile/test_shp.shp")
gdf2 = gpd.read_file("test_shapefile2/test_shp2.shp")


def get_polygon_union(geo_data_frame):
    
    polygons = geo_data_frame['geometry']
    
    merged_polygon = polygons.unary_union
    
    return merged_polygon

union_ply1 = get_polygon_union(gdf)
union_ply2 = get_polygon_union(gdf2)

df = pd.DataFrame({'counrty': ['Norway', 'Germany'], 'geometry': [union_ply1, union_ply2]})

gdf = gpd.GeoDataFrame(df, geometry='geometry')

gdf.crs = 'EPSG:4326'

gdf.to_postgis(name="coverage", con=engine, schema="public", if_exists='append') 

print("success")
