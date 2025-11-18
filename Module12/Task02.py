import urllib.request
import json


def main():
    API_KEY = "de4abc662a28f130b16bca9884ac88e2"

    city = input("Enter city name: ")

    try:
        # Simple direct approach
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read())


        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        name = data['name']

        print(f"\nWeather in {name}:")
        print(f"Temperature: {temp}°C")
        print(f"Conditions: {desc}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()