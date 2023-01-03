from folium.plugins import MarkerCluster

import geopy.exc
import folium

def map_crimes(df: pd.DataFrame) -> bool:
    lim = 1000000
    i = 0
    print("Building the map...")
    map = folium.Map(location=[41.881832, -87.623177], zoom_start=10, tiles="Open street map")
    marker_cluster = folium.plugins.MarkerCluster().add_to(map)
    for index, item in df.iterrows():
        try:
            location = item['LOCATION']
            if isinstance(location, str):
                lat, lon = location[1:-1].split(', ')

                name = item['TYPE'] + ' ' + item['DATETIME']
                folium.Marker((lat, lon), popup=name,
                              icon=folium.Icon(color='darkblue', icon_color='white', icon='male', angle=0,
                                               prefix='fa')).add_to(marker_cluster)
                i += 1
                if i > lim:
                    break
        except geopy.exc.GeocoderUnavailable:
            continue

    print(f"There are {i} points")
    print("Saving the map...")
    map.save('maps/ChicagoCrimesMap.html')
    return True