import requests


URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "hacker23123123"

}

parameters = {
    "query": "ran for 2.7 miles"
}

response = requests.post(url=URL, headers=headers, json=parameters)
result = response.json()

print(result)