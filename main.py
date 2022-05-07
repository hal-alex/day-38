import requests
from datetime import datetime


user_activity_input = input("Tell me what sporting activity you did today: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "hacker23123123"

}

parameters = {
    "query": user_activity_input
}

response = requests.post(url=FITNESS_APP_URL, headers=headers, json=parameters)
result = response.json()
# activity = result["exercises"][0]["name"].title()
# duration = result["exercises"][0]["duration_min"]
# calories = result["exercises"][0]["nf_calories"]
# print(result)
# print(activity)
# print(duration)
# print(calories)


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

headers = {
    "Authorization": "Bearer lk1j23hkj12h312jk3h12kjhkj46h45kj6h7kljh34kj5h34lk5jh34lk5jh"
}


for exercise in result["exercises"]:
    sheety_payload = {
        "sheet1": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }

    }

    adding_to_sheet = requests.post(url=SHEETY_APP_URL, json=sheety_payload, headers=headers)
    print(adding_to_sheet.text)

