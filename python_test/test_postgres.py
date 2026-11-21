
import psycopg
from getpass import getpass

password = getpass("Enter PostgreSQL password: ")

try:
    with psycopg.connect(
        dbname="development_db",
        user="postgres",
        password=password,
        host="localhost",
        port=5432
    ) as conn:

        result = conn.execute(
            "SELECT current_database(), version();"
        ).fetchone()

        print("\nConnection Successful!")
        print("Database:", result[0])
        print("PostgreSQL:", result[1].split(",")[0])

except psycopg.OperationalError as error:
    print("\nConnection Failed!")
    print(error)
