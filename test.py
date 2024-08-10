import requests
import json

url = "https://collector-otp-prod.camsys-apps.com/schedule/MTASBWY/stopsForRoute?apikey=qeqy84JE7hUKfaI0Lxm2Ttcm6ZA0bYrP&&routeId=MTASBWY:R"

r =  requests.get(url)

resp = r.json()

with open("output.json", "w") as f:
    json.dump(resp, f)