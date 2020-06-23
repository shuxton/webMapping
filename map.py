import folium
import pandas

data=pandas.read_csv("Volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])


map=folium.Map(location=[12.907647,77.524713],zoom_start=6,tiles="Stamen Terrain")


fg=folium.FeatureGroup(name="My Map")
for lt, ln , el in zip(lat,lon,elev):
    if el<=1000:
        fg.add_child(folium.Marker(location=[lt,ln],popup=str(el)+"m"  ,icon=folium.Icon(color="green")))
    else:
        fg.add_child(folium.Marker(location=[lt,ln],popup=str(el)+"m"  ,icon=folium.Icon(color="red")))

fg.add_child(folium.GeoJson(data=open("world.json","r",encoding="utf-8-sig").read(),
style_function=lambda x: {"fillColor":"yellow" if x['properties']['POP2005']<10000000 else 'orange '}))

map.add_child(fg)
map.add_child(folium.LayerControl())
 
map.save("map1.html")