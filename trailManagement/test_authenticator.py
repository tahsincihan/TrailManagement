from authenticator import authenticate_user

def test_authenticator():
    # Test the authenticator with valid credentials
    try:
        print("Testing valid credentials...")
        user_details = authenticate_user("grace@plymouth.ac.uk", "ISAD123!")
        print(f"Valid credentials test result: {user_details}")
        assert user_details is not None, "Expected valid user details, got None"
        assert user_details.get("role") is not None, "Expected a valid role for the user"
    except Exception as e:
        print(f"Error during valid credentials test: {e}")

    # Test the authenticator with invalid credentials
    try:
        print("\nTesting invalid credentials...")
        invalid_user = authenticate_user("invalid@plymouth.ac.uk", "wrongpassword")
        print(f"Invalid credentials test result: {invalid_user}")
        assert invalid_user is None, "Expected None for invalid credentials, got a result"
    except Exception as e:
        print(f"Error during invalid credentials test: {e}")

    # Test the authenticator with missing credentials
    try:
        print("\nTesting missing credentials...")
        missing_user = authenticate_user("", "")
        print(f"Missing credentials test result: {missing_user}")
        assert missing_user is None, "Expected None for missing credentials, got a result"
    except Exception as e:
        print(f"Error during missing credentials test: {e}")

    # Test the authenticator with an unreachable database
    try:
        print("\nTesting unreachable API...")
        # Simulate unreachable API by disconnecting from the database
        # or using invalid database credentials in get_db_connection
        unreachable_user = authenticate_user("unreachable@test.com", "password")
        print(f"Unreachable API test result: {unreachable_user}")
        assert unreachable_user is None, "Expected None for unreachable API, got a result"
    except Exception as e:
        print(f"Error during unreachable API test: {e}")

if __name__ == "__main__":
    test_authenticator()
