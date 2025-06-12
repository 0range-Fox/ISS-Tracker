import requests
import folium
import webview

#Here gets info from the API
response = requests.get('http://api.open-notify.org/iss-now.json')

iss_location = response.json()

print(iss_location)
#Here gets the ISS Longitude & Latitude
iss_longitude = iss_location['iss_position']['longitude']

iss_latitude = iss_location['iss_position']['latitude']

#Here prints the ISS location
print("The ISS Location is at:" \
f"Latitude: {iss_latitude} " \
f"Longtitude: {iss_longitude}")

m = folium.Map(location=[float(iss_latitude), float(iss_longitude)])
icon = folium.CustomIcon("https://upload.wikimedia.org/wikipedia/commons/d/d0/International_Space_Station.svg", icon_size=(50, 50))
folium.Marker(location=[float(iss_latitude), float(iss_longitude)], icon=icon,popup="ISS Location").add_to(m)

#Here creates the Website and GUI
m.save("iss_map.html")
webview.create_window('ISS Tracker', 'iss_map.html')
webview.start()