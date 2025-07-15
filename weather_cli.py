import requests

API_KEY = "9b7b83eea5a480d9f7d890cab7a4c81b"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        if data.get("cod") != 200:
            print(f"Error: {data.get('message', 'Unknown error')}")
            return None
        return data
    except requests.RequestException as e:
        print(f"Network error: {e}")
        return None

def display_weather(data):
    city = data["name"]
    country = data["sys"]["country"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    condition = data["weather"][0]["description"].capitalize()
    print(f"\nWeather in {city}, {country}:")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {condition}")

def main():
    print("=== Command-Line Weather App ===")
    city = input("Enter city name: ").strip()
    if not city:
        print("City name cannot be empty.")
        return
    data = get_weather(city)
    if data:
        display_weather(data)

if __name__ == "__main__":
    main() 