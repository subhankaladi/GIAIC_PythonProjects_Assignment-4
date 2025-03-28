import hashlib

def hash_password(password):
    """Returns the SHA-256 hash of the given password."""
    return hashlib.sha256(password.encode()).hexdigest()

def login(email, password_to_check, stored_logins):
    """
    Checks if the given email's stored password hash matches the hash of the password_to_check.
    Returns True if the login is successful, else False.
    """
    if email in stored_logins:  # Check if email exists in stored logins
        stored_hash = stored_logins[email]  # Get stored hash
        return stored_hash == hash_password(password_to_check)  # Compare hashes
    return False  # Return False if email not found

def main():
    # Stored logins (email: hashed password)
    stored_logins = {
        "user@example.com": hash_password("securepassword123"),
        "kaladi@dev.com": hash_password("mysecretpass"),
    }

    # User input
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    # Check login
    if login(email, password, stored_logins):
        print("Login successful! ✅")
    else:
        print("Login failed! ❌ Incorrect email or password.")

# Required line to run the main() function
if __name__ == '__main__':
    main()

