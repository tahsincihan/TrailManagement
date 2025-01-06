from crud_operations import create_trail, read_trail, update_trail, delete_trail
from database_connection import get_db_connection

def test_crud_operations():
    # Establish database connection
    conn = get_db_connection()
    if conn is None:
        print("Database connection failed. Exiting...")
        return

    try:
        # CREATE: Add a new trail
        print("Testing CREATE operation...")
        new_trail_data = {
            "TrailName": "New Test Trail",
            "TrailSummary": "Summary for a new test trail.",
            "TrailDescription": "This is a description for a new test trail.",
            "Difficulty": "Easy",
            "Location": "Test Location",
            "Length": 4.20,
            "ElevationGain": 120.00,
            "RouteID": 1
        }
        create_trail(conn, **new_trail_data)
        print("CREATE operation successful.")

        # READ: Fetch the newly created trail
        print("\nTesting READ operation...")
        cursor = conn.cursor()
        cursor.execute("SELECT MAX(TrailID) FROM CW2.Trail")
        new_trail_id = cursor.fetchone()[0]
        trail = read_trail(conn, new_trail_id)
        print(f"READ operation result: {trail}")

        # UPDATE: Modify the trail
        print("\nTesting UPDATE operation...")
        updated_data = {
            "TrailName": "Updated Test Trail",
            "TrailDescription": "Updated description for the test trail."
        }
        update_trail(conn, new_trail_id, **updated_data)
        updated_trail = read_trail(conn, new_trail_id)
        print(f"Trail after UPDATE: {updated_trail}")

        # DELETE: Remove the trail
        print("\nTesting DELETE operation...")
        delete_trail(conn, new_trail_id)
        deleted_trail = read_trail(conn, new_trail_id)
        print(f"Trail after DELETE (should be None): {deleted_trail}")

    except Exception as e:
        print(f"Error during CRUD operation testing: {e}")
    finally:
        conn.close()
        print("Database connection closed.")

if __name__ == "__main__":
    test_crud_operations()
