import requests
import json
import time

routes = list("1234567ACEBDFMGJZLNQRW") + ["GS", "H", "FS", "SI"]

url = "https://collector-otp-prod.camsys-apps.com/schedule/MTASBWY/stopsForRoute?apikey=qeqy84JE7hUKfaI0Lxm2Ttcm6ZA0bYrP&&routeId=MTASBWY:{0}"

session = requests.Session()

output = {}

for route in routes:
    print(f"Queuing route ID: {route}")
    rq = session.get(url.format(route))
    j = rq.json()

    time.sleep(1)

    if len(j) == 0:
        print(f"No stops found for {route}")
        continue

    l = [d["stopId"] for d in j]
    output[f"MTASBWY:{route}"] = l

with open("output.json", "w") as f:
    json.dump(output, f, indent = 4)

# print(routes)