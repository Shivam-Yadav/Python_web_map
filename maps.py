__author__ = 'Shivam'
import folium        #import library
import pandas        #import pandas lib for reading data off files

df=pandas.read_csv('Volcanoes-USA.txt')   #create a dataframe object

map = folium.Map(location=[df['LAT'].mean(), df['LON'].mean()], zoom_start=4, tiles='Stamen Terrain')  # create map

'''def color(elev):
     if elev in range(0,1000):
         col='green'
     elif elev in range(1000,3000):
         col='yellow'
     elif elev in range(3000,4000):
         col='red'
     else:
         col='black'
     return col
'''
def color(elev):
     minimum=min(df['ELEV'])
     maximum=max(df['ELEV'])
     step = (maximum-minimum)/4
     if elev in range(int(minimum) , int (minimum+step)):
         col='green'
     elif elev in range(int (minimum+step),int (minimum+step*2)):
         col='orange'
     elif elev in range(int (minimum+step*2), int (minimum+step*3)):
         col='red'
     else:
         col='black'
     return col

fg=folium.FeatureGroup(name='Volcano Locations')

for lat,lon,name,elev in zip(df['LAT'],df['LON'],df['NAME'],df['ELEV']):  #when looping with 2 or more iterators, we use zip, LAT n LON are defined in txt file
    fg.add_child(folium.Marker(location=[lat, lon], popup=name, icon=folium.Icon(color=color(elev)) ))

map.add_child(fg)

map.add_child(folium.GeoJson(data=open('shape.json'), name='world_pop',\
style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005']<=50000000 else 'blue' if 50000000< x['properties']['POP2005']<=1000000000\
    else 'red'}))

map.add_child(folium.LayerControl())
map.save(outfile='test.html')
