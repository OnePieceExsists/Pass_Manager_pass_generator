class PasswordGenerator:
    import random
    import string

    def generate_password(self, length=12, use_uppercase=True, use_numbers=True, use_special_chars=True):
        characters = string.ascii_lowercase
        if use_uppercase:
            characters += string.ascii_uppercase
        if use_numbers:
            characters += string.digits
        if use_special_chars:
            characters += string.punctuation

        password = ''.join(random.choice(characters) for _ in range(length))
        return password