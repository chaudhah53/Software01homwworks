import sqlite3

def main():
    conn = sqlite3.connect("airport.db")
    cursor = conn.cursor()
    country = input("Enter the country code (e.g. FI): ").strip().upper()
    cursor.execute("""
        SELECT type, COUNT(*) 
        FROM airport 
        WHERE iso_country = ? 
        GROUP BY type 
        ORDER BY type
    """, (country,))
    results = cursor.fetchall()
    if results:
        for airport_type, count in results:
            print(f"{airport_type}: {count}")
    else:
        print("No airports found for that country code.")
    conn.close()

if __name__ == "__main__":
    main()
