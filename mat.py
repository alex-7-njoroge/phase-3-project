import psycopg2

# Database connection
def get_connection():
    return psycopg2.connect(
         dbname='matwana',
    user='postgres',
    password='1234',
    host='localhost',
    port='5432'
    )

# Vehicle Management
def create_vehicle_table():
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS vehicles (
                vehicle_id SERIAL PRIMARY KEY,
                licenseplate VARCHAR(20),
                status VARCHAR(10) CHECK (status IN ('Nganya', 'Mboko', 'Gari'))
            )
        """)
    conn.commit()
    conn.close()

def add_vehicle(licenseplate, status):
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO vehicles (licenseplate, status) VALUES (%s, %s)", 
                       (licenseplate, status))
    conn.commit()
    conn.close()

def view_vehicles():
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM vehicles")
        return cursor.fetchall()
    conn.close()

# Route Management
def create_route_table():
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS routes (
                route_id SERIAL PRIMARY KEY,
                start_point VARCHAR(100),
                end_point VARCHAR(100)
            )
        """)
    conn.commit()
    conn.close()

def add_route(start_point, end_point):
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO routes (start_point, end_point) VALUES (%s, %s)", 
                       (start_point, end_point))
    conn.commit()
    conn.close()

def view_routes():
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM routes")
        return cursor.fetchall()
    conn.close()

# Driver Management
def create_driver_table():
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS drivers (
                driver_id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                contacts VARCHAR(100)
            )
        """)
    conn.commit()
    conn.close()

def add_driver(name, contacts):
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO drivers (name, contacts) VALUES (%s, %s)", 
                       (name, contacts))
    conn.commit()
    conn.close()

def view_drivers():
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM drivers")
        return cursor.fetchall()
    conn.close()

# Main Application
def main():
    create_vehicle_table()
    create_route_table()
    create_driver_table()

    while True:
        print("\nWabebe Transport System")
        print("1. Manage Vehicles")
        print("2. Manage Routes")
        print("3. Manage Drivers")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            print("1. Add Vehicle")
            print("2. View Vehicles")
            vehicle_choice = input("Select an option: ")
            if vehicle_choice == '1':
                licenseplate = input("Enter license plate: ")
                status = input("Enter status (Nganya, Mboko, Gari): ")
                add_vehicle(licenseplate, status)
                print("Vehicle added successfully.")
            elif vehicle_choice == '2':
                vehicles = view_vehicles()
                for vehicle in vehicles:
                    print(vehicle)

        elif choice == '2':
            print("1. Add Route")
            print("2. View Routes")
            route_choice = input("Select an option: ")
            if route_choice == '1':
                start_point = input("Enter start point: ")
                end_point = input("Enter end point: ")
                add_route(start_point, end_point)
                print("Route added successfully.")
            elif route_choice == '2':
                routes = view_routes()
                for route in routes:
                    print(route)

        elif choice == '3':
            print("1. Add Driver")
            print("2. View Drivers")
            driver_choice = input("Select an option: ")
            if driver_choice == '1':
                name = input("Enter name: ")
                contacts = input("Enter contacts: ")
                add_driver(name, contacts)
                print("Driver added successfully.")
            elif driver_choice == '2':
                drivers = view_drivers()
                for driver in drivers:
                    print(driver)

        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
