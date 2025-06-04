def is_strong_password(password):
    """Check if the password is strong."""
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char in "!@#$%^&*()-_=+[]{}|;:,.<>?/" for char in password):
        return False
    return True

def format_password(password):
    """Format the password for display."""
    return password.strip()

def validate_password_strength(password):
    """Validate the strength of the password."""
    if is_strong_password(password):
        return "Strong password"
    else:
        return "Weak password"