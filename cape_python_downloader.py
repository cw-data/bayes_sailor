import requests

url = "https://raw.githubusercontent.com/rlvaugh/Real_World_Python/master/Chapter_1/cape_python.png"
r = requests.get(url)
open('cape_python.png', 'wb').write(r.content)