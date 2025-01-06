from flask import Flask, request, jsonify, render_template
from flask_restful import Api, Resource
from flask_cors import CORS
from flasgger import Swagger
from database_connection import get_db_connection
from crud_operations import create_trail, read_trail, update_trail, delete_trail
import jwt
import datetime
import logging

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS
api = Api(app)  # Initialize Flask-RESTful API
swagger = Swagger(app, template_file="swagger.yml")  # Initialize Swagger

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Secret key for JWT
SECRET_KEY = "your_secret_key"

# Database connection
conn = get_db_connection()
if conn is None:
    raise ConnectionError("Database connection failed. Check your database settings.")

# Function to generate JWT tokens
def generate_token(user_id, role):
    """Generates a JWT token."""
    payload = {
        "user_id": user_id,
        "role": role,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Token valid for 1 hour
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

# Function to validate JWT tokens
def validate_token(auth_header):
    """Validates JWT tokens."""
    if not auth_header or not auth_header.startswith("Bearer "):
        return {"error": "Unauthorized access"}, 403

    token = auth_header.split(" ")[1]
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return decoded_token
    except jwt.ExpiredSignatureError:
        return {"error": "Token has expired"}, 401
    except jwt.InvalidTokenError:
        return {"error": "Invalid token"}, 403

# Routes
@app.route("/")
def home():
    """Home route."""
    return render_template("index.html")

@app.route("/auth", methods=["POST"])
def login():
    """Handles login and returns a JWT token."""
    data = request.json
    email = data.get("email")
    password = data.get("password")
    if not email or not password:
        return jsonify({"error": "Email and password are required."}), 400

    # Fake user authentication
    if email == "admin@example.com" and password == "password":
        token = generate_token(user_id=1, role="admin")
        return jsonify({"token": token})
    elif email == "user@example.com" and password == "password":
        token = generate_token(user_id=2, role="user")
        return jsonify({"token": token})
    else:
        return jsonify({"error": "Invalid credentials"}), 401

# TrailList Resource
class TrailList(Resource):
    def get(self):
        """Fetch all trails."""
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM CW2.Trail")
            rows = cursor.fetchall()
            trails = [dict(zip([col[0] for col in cursor.description], row)) for row in rows]
            return jsonify(trails)
        except Exception as e:
            logging.error(f"Error fetching trails: {e}")
            return jsonify({"error": str(e)}), 500

    def post(self):
        """Create a new trail (Admin only)."""
        auth_header = request.headers.get("Authorization")
        decoded_token = validate_token(auth_header)
        if isinstance(decoded_token, tuple):
            return jsonify(decoded_token[0]), decoded_token[1]

        if decoded_token["role"].lower() != "admin":
            return jsonify({"error": "Admin privileges required."}), 403

        data = request.json
        try:
            create_trail(conn, **data)
            return jsonify({"message": "Trail created successfully!"}), 201
        except Exception as e:
            logging.error(f"Error creating trail: {e}")
            return jsonify({"error": str(e)}), 500

# TrailDetail Resource
class TrailDetail(Resource):
    def get(self, trail_id):
        """Fetch a specific trail by ID."""
        try:
            trail = read_trail(conn, trail_id)
            if not trail:
                return jsonify({"message": "Trail not found"}), 404
            return jsonify(trail)
        except Exception as e:
            logging.error(f"Error fetching trail: {e}")
            return jsonify({"error": str(e)}), 500

    def put(self, trail_id):
        """Update a specific trail (Admin only)."""
        auth_header = request.headers.get("Authorization")
        decoded_token = validate_token(auth_header)
        if isinstance(decoded_token, tuple):
            return jsonify(decoded_token[0]), decoded_token[1]

        if decoded_token["role"].lower() != "admin":
            return jsonify({"error": "Admin privileges required."}), 403

        data = request.json
        try:
            update_trail(conn, trail_id, **data)
            return jsonify({"message": "Trail updated successfully!"})
        except Exception as e:
            logging.error(f"Error updating trail: {e}")
            return jsonify({"error": str(e)}), 500

    def delete(self, trail_id):
        """Delete a specific trail (Admin only)."""
        auth_header = request.headers.get("Authorization")
        decoded_token = validate_token(auth_header)
        if isinstance(decoded_token, tuple):
            return jsonify(decoded_token[0]), decoded_token[1]

        if decoded_token["role"].lower() != "admin":
            return jsonify({"error": "Admin privileges required."}), 403

        try:
            delete_trail(conn, trail_id)
            return jsonify({"message": "Trail deleted successfully!"})
        except Exception as e:
            logging.error(f"Error deleting trail: {e}")
            return jsonify({"error": str(e)}), 500

# Register resources
api.add_resource(TrailList, "/trails")
api.add_resource(TrailDetail, "/trails/<int:trail_id>")

if __name__ == "__main__":
    print("Swagger UI available at: http://127.0.0.1:5000/apidocs")
    app.run(debug=True)
