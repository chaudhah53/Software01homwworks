import sqlite3
from geopy.distance import geodesic

def main():
    conn = sqlite3.connect("airport.db")
    cursor = conn.cursor()

    icao1 = input("Enter the ICAO code of the first airport: ").strip().upper()
    icao2 = input("Enter the ICAO code of the second airport: ").strip().upper()

    cursor.execute("SELECT latitude_deg, longitude_deg FROM airport WHERE ident = ?", (icao1,))
    airport1 = cursor.fetchone()

    cursor.execute("SELECT latitude_deg, longitude_deg FROM airport WHERE ident = ?", (icao2,))
    airport2 = cursor.fetchone()

    if airport1 and airport2:
        coord1 = (airport1[0], airport1[1])
        coord2 = (airport2[0], airport2[1])
        distance_km = geodesic(coord1, coord2).kilometers
        print(f"Distance between {icao1} and {icao2}: {distance_km:.2f} km")
    else:
        print("Could not find coordinates for one or both ICAO codes.")

    conn.close()

if __name__ == "__main__":
    main()
