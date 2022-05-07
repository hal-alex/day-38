import requests



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
activity = result["exercises"][0]["name"].title()
duration = result["exercises"][0]["duration_min"]
calories = result["exercises"][0]["nf_calories"]
print(result)
print(activity)
print(duration)
print(calories)

sheety_payload = {
    "sheet1": {
        "date": 10,
        "time": 10,
        "exercise": activity,
        "duration": duration,
        "calories": calories,
    }

}

adding_to_sheet = requests.post(url=SHEETY_APP_URL, json=sheety_payload)
print(adding_to_sheet)

