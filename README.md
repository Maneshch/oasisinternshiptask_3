# Command-Line Weather App

A simple Python command-line application that fetches and displays current weather data for a user-specified city using the OpenWeatherMap API.

## Features
- Fetches current weather for any city
- Displays temperature (°C), humidity (%), and weather conditions
- Handles errors gracefully (invalid city, network issues, etc.)

## Requirements
- Python 3.x
- `requests` library (install with `pip install requests`)
- OpenWeatherMap API key (free)

## Setup
1. **Clone or download this repository.**
2. **Install dependencies:**
   ```bash
   pip install requests
   ```
3. **Get a free API key from [OpenWeatherMap](https://home.openweathermap.org/users/sign_up).**
   - After signing up, check your email and activate your account.
   - Copy your API key from the [API keys page](https://home.openweathermap.org/api_keys).
   - Paste your API key into the `API_KEY` variable in `weather_cli.py`.

## Usage
1. Open a terminal and navigate to the project directory:
   ```bash
   cd weatherApp
   ```
2. Run the script:
   ```bash
   python weather_cli.py
   ```
3. Enter the city name when prompted (e.g., `London`, `New York`).
4. View the current weather information.

## Notes
- If you see a `401 Unauthorized` error, your API key may not be activated yet. Wait a few hours after registration.
- You can change the temperature unit to Fahrenheit by modifying the `units` parameter in the script.

## Example
```
=== Command-Line Weather App ===
Enter city name: Paris

Weather in Paris, FR:
Temperature: 18°C
Humidity: 60%
Condition: Clear sky
```

---

Feel free to improve or extend this app (add forecasts, unit conversion, or a GUI)! 
