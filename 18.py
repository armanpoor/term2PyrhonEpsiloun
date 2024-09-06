import requests
import json

api_key = "610236741ad896925e95e43ff0cbd0c2"

# نام شهر و کشور
city_name = input("lotfan nam shahr ra vared konid: ")
country_code = "IR"

# ساخت URL درخواست
url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name},{country_code}&appid={api_key}&units=metric"

# ارسال درخواست به API
response = requests.get(url)
content = response.content
desire_dict = json.loads(content)
humadity = desire_dict["main"]["humidity"]
print(f"rootobat hava dar shar {city_name}: {humadity}")

