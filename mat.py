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
        cursor.execute("""
            SELECT v.vehicle_id, v.licenseplate, v.status, 
                   d.name, d.contacts, 
                   r.start_point, r.end_point
            FROM vehicles v
            LEFT JOIN drivers d ON v.vehicle_id = d.driver_id
            LEFT JOIN routes r ON v.vehicle_id = r.route_id
        """)
        vehicles = cursor.fetchall()
        for vehicle in vehicles:
            print(f"ID: {vehicle[0]}, License Plate: {vehicle[1]}, Status: {vehicle[2]}, "
                  f"Driver: {vehicle[3] or 'N/A'}, Contacts: {vehicle[4] or 'N/A'}, "
                  f"Route: {vehicle[5] or 'N/A'} to {vehicle[6] or 'N/A'}")
    conn.close()

def update_vehicle(vehicle_id, licenseplate, status):
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("""
            UPDATE vehicles
            SET licenseplate = %s, status = %s
            WHERE vehicle_id = %s
        """, (licenseplate, status, vehicle_id))
    conn.commit()
    conn.close()

def delete_vehicle(vehicle_id):
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM vehicles WHERE vehicle_id = %s", (vehicle_id,))
    conn.commit()
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
        routes = cursor.fetchall()
        for route in routes:
            print(f"Route ID: {route[0]}, Start Point: {route[1]}, End Point: {route[2]}")
    conn.close()

def update_route(route_id, start_point, end_point):
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("""
            UPDATE routes
            SET start_point = %s, end_point = %s
            WHERE route_id = %s
        """, (start_point, end_point, route_id))
    conn.commit()
    conn.close()

def delete_route(route_id):
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM routes WHERE route_id = %s", (route_id,))
    conn.commit()
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
        drivers = cursor.fetchall()
        for driver in drivers:
            print(f"Driver ID: {driver[0]}, Name: {driver[1]}, Contacts: {driver[2]}")
    conn.close()

def update_driver(driver_id, name, contacts):
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("""
            UPDATE drivers
            SET name = %s, contacts = %s
            WHERE driver_id = %s
        """, (name, contacts, driver_id))
    conn.commit()
    conn.close()

def delete_driver(driver_id):
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM drivers WHERE driver_id = %s", (driver_id,))
    conn.commit()
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
            print("3. Update Vehicle")
            print("4. Delete Vehicle")
            vehicle_choice = input("Select an option: ")
            if vehicle_choice == '1':
                licenseplate = input("Enter license plate: ")
                status = input("Enter status (Nganya, Mboko, Gari): ")
                add_vehicle(licenseplate, status)
                print("Vehicle added successfully.")
            elif vehicle_choice == '2':
                view_vehicles()  # Formatted output
            elif vehicle_choice == '3':
                vehicle_id = int(input("Enter vehicle ID to update: "))
                licenseplate = input("Enter new license plate: ")
                status = input("Enter new status (Nganya, Mboko, Gari): ")
                update_vehicle(vehicle_id, licenseplate, status)
                print("Vehicle updated successfully.")
            elif vehicle_choice == '4':
                vehicle_id = int(input("Enter vehicle ID to delete: "))
                delete_vehicle(vehicle_id)
                print("Vehicle deleted successfully.")

        elif choice == '2':
            print("1. Add Route")
            print("2. View Routes")
            print("3. Update Route")
            print("4. Delete Route")
            route_choice = input("Select an option: ")
            if route_choice == '1':
                start_point = input("Enter start point: ")
                end_point = input("Enter end point: ")
                add_route(start_point, end_point)
                print("Route added successfully.")
            elif route_choice == '2':
                view_routes()  # Formatted output
            elif route_choice == '3':
                route_id = int(input("Enter route ID to update: "))
                start_point = input("Enter new start point: ")
                end_point = input("Enter new end point: ")
                update_route(route_id, start_point, end_point)
                print("Route updated successfully.")
            elif route_choice == '4':
                route_id = int(input("Enter route ID to delete: "))
                delete_route(route_id)
                print("Route deleted successfully.")

        elif choice == '3':
            print("1. Add Driver")
            print("2. View Drivers")
            print("3. Update Driver")
            print("4. Delete Driver")
            driver_choice = input("Select an option: ")
            if driver_choice == '1':
                name = input("Enter name: ")
                contacts = input("Enter contacts: ")
                add_driver(name, contacts)
                print("Driver added successfully.")
            elif driver_choice == '2':
                view_drivers()  # Formatted output
            elif driver_choice == '3':
                driver_id = int(input("Enter driver ID to update: "))
                name = input("Enter new name: ")
                contacts = input("Enter new contacts: ")
                update_driver(driver_id, name, contacts)
                print("Driver updated successfully.")
            elif driver_choice == '4':
                driver_id = int(input("Enter driver ID to delete: "))
                delete_driver(driver_id)
                print("Driver deleted successfully.")

        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
