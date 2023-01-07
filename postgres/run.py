from sqlalchemy import create_engine
import geopandas as gpd
 
user = "postgres"
password = "testtest"
host = "localhost"
port = 5432
database = "postgres"
 
conn = f"postgresql://{user}:{password}@{host}:{port}/{database}"
engine = create_engine(conn)
 
#Read shapefile using GeoPandas
gdf = gpd.read_file("test_shapefile/test_shp.shp")
gdf2 = gpd.read_file("test_shapefile2/test_shp2.shp")
 
#Import shapefile to databse
gdf.to_postgis(name="fields", con=engine, schema="public", if_exists='append')
gdf2.to_postgis(name="fields", con=engine, schema="public", if_exists='append')

 
print("success")

#pipenv install psycopg2-binary
#pipenv install sqlalchemy
#pipenv install geopandas
#pipenv install GeoAlchemy2

""" SELECT ST_AsGeoJSON(geometry)
FROM fields
WHERE ST_Contains(geometry, ST_SetSRID(ST_MakePoint(:longitude, :latitude), 4326)) """