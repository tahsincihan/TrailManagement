import pyodbc

def create_trail(conn, trail_name, trail_summary, trail_description, difficulty, location, length, elevation_gain, route_id):
    """
    Inserts a new trail into the Trail table.
    """
    try:
        cursor = conn.cursor()
        query = """
            INSERT INTO CW2.Trail (TrailName, TrailSummary, TrailDescription, Difficulty, Location, Length, ElevationGain, RouteID)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(query, (trail_name, trail_summary, trail_description, difficulty, location, length, elevation_gain, route_id))
        conn.commit()
        return {"message": "Trail created successfully"}
    except pyodbc.Error as e:
        print(f"Error creating trail: {e}")
        raise

def read_trail(conn, trail_id=None):
    """
    Fetches all trails or a specific trail by ID.
    """
    try:
        cursor = conn.cursor()
        if trail_id:
            query = "SELECT * FROM CW2.Trail WHERE TrailID = ?"
            cursor.execute(query, (trail_id,))
            row = cursor.fetchone()
            if row:
                return dict(zip([column[0] for column in cursor.description], row))
            else:
                return None
        else:
            query = "SELECT * FROM CW2.Trail"
            cursor.execute(query)
            rows = cursor.fetchall()
            return [dict(zip([column[0] for column in cursor.description], row)) for row in rows]
    except pyodbc.Error as e:
        print(f"Error reading trail: {e}")
        raise

def update_trail(conn, trail_id, trail_name=None, trail_summary=None, trail_description=None,
                 difficulty=None, location=None, length=None, elevation_gain=None, route_id=None):
    """
    Updates a specific trail by ID.
    """
    try:
        cursor = conn.cursor()
        query = "UPDATE CW2.Trail SET "
        updates = []
        params = []

        if trail_name:
            updates.append("TrailName = ?")
            params.append(trail_name)
        if trail_summary:
            updates.append("TrailSummary = ?")
            params.append(trail_summary)
        if trail_description:
            updates.append("TrailDescription = ?")
            params.append(trail_description)
        if difficulty:
            updates.append("Difficulty = ?")
            params.append(difficulty)
        if location:
            updates.append("Location = ?")
            params.append(location)
        if length:
            updates.append("Length = ?")
            params.append(length)
        if elevation_gain:
            updates.append("ElevationGain = ?")
            params.append(elevation_gain)
        if route_id:
            updates.append("RouteID = ?")
            params.append(route_id)

        if not updates:
            return {"message": "No fields to update"}

        query += ", ".join(updates) + " WHERE TrailID = ?"
        params.append(trail_id)

        cursor.execute(query, params)
        conn.commit()
        return {"message": "Trail updated successfully"}
    except pyodbc.Error as e:
        print(f"Error updating trail: {e}")
        raise

def delete_trail(conn, trail_id):
    """
    Deletes a trail by ID.
    """
    try:
        cursor = conn.cursor()
        query = "DELETE FROM CW2.Trail WHERE TrailID = ?"
        cursor.execute(query, (trail_id,))
        conn.commit()
        return {"message": "Trail deleted successfully"}
    except pyodbc.Error as e:
        print(f"Error deleting trail: {e}")
        raise
