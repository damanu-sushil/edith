import requests


def get_current_city():
    try:
        response = requests.get("https://ipinfo.io/json")
        response.raise_for_status()
        data = response.json()
        return data['city']
    except requests.RequestException as e:
        print("Error fetching location:", e)
        return None

# Step 2: Fetch the weather forecast for a given city
def get_weather(city):
    url = f"https://wttr.in/{city}?format=%C+%t+%w"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text.strip()
    except requests.RequestException as e:
        print("Error fetching the weather:", e)
        return None