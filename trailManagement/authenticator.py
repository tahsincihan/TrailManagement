import hashlib
import pyodbc


def get_db_connection():
    """Connect to the database."""
    try:
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=dist-6-505.uopnet.plymouth.ac.uk;'
            'DATABASE=your_database;'
            'UID=your_user;'
            'PWD=your_password'
        )
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None


def hash_password(password):
    """Hash the password using SHA256."""
    return hashlib.sha256(password.encode()).hexdigest()


def authenticate_user(email, password):
    """
    Authenticate a user by verifying their email and password.

    Args:
        email (str): The user's email address.
        password (str): The user's password.

    Returns:
        dict: User information if authenticated, None otherwise.
    """
    conn = get_db_connection()
    if not conn:
        return None

    hashed_password = hash_password(password)

    try:
        cursor = conn.cursor()
        query = """
            SELECT UserID, Role 
            FROM CW2.Users 
            WHERE Email = ? AND PasswordHash = ?
        """
        cursor.execute(query, (email, hashed_password))
        user = cursor.fetchone()

        if user:
            return {
                "user_id": user.UserID,
                "role": user.Role
            }
        else:
            print("Invalid email or password.")
            return None
    except Exception as e:
        print(f"Error during authentication: {e}")
        return None
    finally:
        conn.close()
