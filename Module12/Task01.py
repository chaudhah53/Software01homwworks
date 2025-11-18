import urllib.request
import json
import ssl


def get_random_chuck_norris_joke():
    try:
        context = ssl.create_default_context()
        url = "https://api.chucknorris.io/jokes/random"

        req = urllib.request.Request(
            url,
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                'Accept': 'application/json'
            }
        )

        with urllib.request.urlopen(req, context=context, timeout=10) as response:
            if response.status == 200:
                data = response.read().decode('utf-8')
                joke_data = json.loads(data)
                return joke_data['value']
            else:
                return f"Error: Received status code {response.status}"

    except urllib.error.URLError as e:
        return f"Network Error: {e.reason}"
    except json.JSONDecodeError as e:
        return f"Data Error: Could not parse response"
    except Exception as e:
        return f"Unexpected error: {e}"


def main():
    print("=== Random Chuck Norris Joke ===")
    print("Fetching a joke...")

    joke = get_random_chuck_norris_joke()

    print("\n" + "=" * 50)
    print(joke)
    print("=" * 50)


if __name__ == "__main__":
    main()