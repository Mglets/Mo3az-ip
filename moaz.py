

import requests

print("entar ip.")

ip = input("عنوان IP: ")

try:
    response = requests.get(f"http://ip-api.com/json/{ip}")
    data = response.json()

    country = data["country"]
    city = data["city"]
    isp = data["isp"]

    # عرض المعلومات
    print(f"الدولة: {country}")
    print(f"المدينة: {city}")
    print(f"مزود الخدمة: {isp}")
except:
    print("ERROR")
