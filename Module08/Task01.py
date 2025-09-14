import sqlite3

def main():
    conn = sqlite3.connect("airport.db")
    cursor = conn.cursor()
    icao = input("Enter the ICAO code: ").strip().upper()
    cursor.execute("SELECT name, municipality FROM airport WHERE ident = ?", (icao,))
    result = cursor.fetchone()
    if result:
        name, town = result
        print(f"Airport Name: {name}")
        print(f"Location (Town): {town}")
    else:
        print("No airport found with that ICAO code.")
    conn.close()

if __name__ == "__main__":
    main()
