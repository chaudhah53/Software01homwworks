from flask import Flask, jsonify

app = Flask(__name__)

airports = {
    "EFHK": {"Name": "Helsinki-Vantaa Airport", "Location": "Helsinki"},
    "EFJK": {"Name": "Jyväskylä Airport", "Location": "Jyväskylä"},
    "EFOU": {"Name": "Oulu Airport", "Location": "Oulu"},
    "EFTP": {"Name": "Tampere-Pirkkala Airport", "Location": "Tampere"},
    "EFVA": {"Name": "Vaasa Airport", "Location": "Vaasa"},
    "EFRO": {"Name": "Rovaniemi Airport", "Location": "Rovaniemi"},
    "EFTU": {"Name": "Turku Airport", "Location": "Turku"},
    "EFPO": {"Name": "Pori Airport", "Location": "Pori"},
    "EFKT": {"Name": "Kittilä Airport", "Location": "Kittilä"},
    "EFIV": {"Name": "Ivalo Airport", "Location": "Ivalo"},
    "KJFK": {"Name": "John F Kennedy International Airport", "Location": "New York"},
    "KLAX": {"Name": "Los Angeles International Airport", "Location": "Los Angeles"},
    "EGLL": {"Name": "Heathrow Airport", "Location": "London"},
    "LFPG": {"Name": "Charles de Gaulle Airport", "Location": "Paris"},
    "EDDF": {"Name": "Frankfurt am Main Airport", "Location": "Frankfurt"},
    "RJTT": {"Name": "Tokyo Haneda Airport", "Location": "Tokyo"}
}


@app.route('/airport/<icao_code>')
def get_airport_info(icao_code):
    icao_code = icao_code.upper()

    if icao_code in airports:
        airport_data = airports[icao_code]
        response = {
            "ICAO": icao_code,
            "Name": airport_data["Name"],
            "Location": airport_data["Location"]
        }
        return jsonify(response)
    else:
        return jsonify({"error": "Airport not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
