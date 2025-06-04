class PasswordManager:
    def __init__(self):
        self.passwords = {}

    def add_password(self, name, password):
        self.passwords[name] = password

    def retrieve_password(self, name):
        return self.passwords.get(name, None)

    def delete_password(self, name):
        if name in self.passwords:
            del self.passwords[name]