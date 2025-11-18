import urllib.request
import json
import os


def get_weather_data(city_name, api_key):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode('utf-8'))
            return data

    except urllib.error.HTTPError as e:
        if e.code == 401:
            raise Exception("Invalid API Key.")
        elif e.code == 404:
            raise Exception(f"City '{city_name}' not found.")
        elif e.code == 429:
            raise Exception("API rate limit exceeded.")
        else:
            raise Exception(f"HTTP Error {e.code}")
    except Exception as e:
        raise Exception(f"Failed to fetch weather data: {e}")


def display_weather_info(weather_data):
    city = weather_data['name']
    country = weather_data['sys']['country']
    temperature = weather_data['main']['temp']
    feels_like = weather_data['main']['feels_like']
    description = weather_data['weather'][0]['description'].title()
    humidity = weather_data['main']['humidity']

    print("\n" + "=" * 40)
    print(f"Weather in {city}, {country}")
    print("=" * 40)
    print(f"Temperature: {temperature}°C")
    print(f"Feels like: {feels_like}°C")
    print(f"Conditions: {description}")
    print(f"Humidity: {humidity}%")
    print("=" * 40)


def main():
    API_KEY = os.getenv('OPENWEATHER_API_KEY')

    if not API_KEY:
        print("OPENWEATHER_API_KEY environment variable not set.")
        print("Please enter your OpenWeather API key:")
        API_KEY = input("API Key: ").strip()

    if not API_KEY:
        print("Error: API key is required.")
        return

    print("=== Weather Information ===")

    while True:
        city = input("\nEnter city name (or 'quit' to exit): ").strip()

        if city.lower() == 'quit':
            print("Goodbye!")
            break

        if not city:
            print("Please enter a valid city name.")
            continue

        try:
            weather_data = get_weather_data(city, API_KEY)
            display_weather_info(weather_data)

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()