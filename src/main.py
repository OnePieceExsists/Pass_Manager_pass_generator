import tkinter as tk
from tkinter import simpledialog, messagebox
from manager import PasswordManager
from generator import PasswordGenerator

class AddPasswordDialog(simpledialog.Dialog):
    def __init__(self, parent, title=None):
        super().__init__(parent, title)

    def body(self, master):
        self.after(0, lambda: (self.geometry("400x220"), self.resizable(False, False)))
        tk.Label(master, text="Site Name:").pack(pady=(10, 0))
        self.site_var = tk.StringVar()
        tk.Entry(master, textvariable=self.site_var).pack()

        tk.Label(master, text="Password (max 12 chars):").pack(pady=(10, 0))
        self.password_var = tk.StringVar()
        entry = tk.Entry(master, textvariable=self.password_var)
        entry.pack()
        entry.focus_set()
        self.password_var.trace("w", self.limit_length)
        return entry

    def limit_length(self, *args):
        value = self.password_var.get()
        if len(value) > 12:
            self.password_var.set(value[:12])

    def apply(self):
        self.result = {
            "site": self.site_var.get(),
            "password": self.password_var.get()
        }

class RetrievePasswordDialog(simpledialog.Dialog):
    def __init__(self, parent, title=None):
        super().__init__(parent, title)

    def body(self, master):
        self.after(0, lambda: (self.geometry("400x220"), self.resizable(False, False)))
        tk.Label(master, text="Site Name:").pack(pady=(20, 0))
        self.site_var = tk.StringVar()
        entry = tk.Entry(master, textvariable=self.site_var)
        entry.pack()
        entry.focus_set()
        return entry

    def apply(self):
        self.result = self.site_var.get()

class DeletePasswordDialog(simpledialog.Dialog):
    def __init__(self, parent, title=None):
        super().__init__(parent, title)

    def body(self, master):
        self.after(0, lambda: (self.geometry("400x220"), self.resizable(False, False)))
        tk.Label(master, text="Site Name:").pack(pady=(20, 0))
        self.site_var = tk.StringVar()
        entry = tk.Entry(master, textvariable=self.site_var)
        entry.pack()
        entry.focus_set()
        return entry

    def apply(self):
        self.result = self.site_var.get()

class GeneratePasswordDialog(simpledialog.Dialog):
    def __init__(self, parent, title=None):
        super().__init__(parent, title)

    def body(self, master):
        self.after(0, lambda: (self.geometry("400x220"), self.resizable(False, False)))
        tk.Label(master, text="Password Length:").pack(pady=(10, 0))
        self.length_var = tk.IntVar(value=12)
        tk.Entry(master, textvariable=self.length_var).pack()

        self.symbols_var = tk.BooleanVar(value=True)
        tk.Checkbutton(master, text="Include Symbols", variable=self.symbols_var).pack(anchor="w", padx=20)

        self.numbers_var = tk.BooleanVar(value=True)
        tk.Checkbutton(master, text="Include Numbers", variable=self.numbers_var).pack(anchor="w", padx=20)

    def apply(self):
        self.result = {
            "length": self.length_var.get(),
            "symbols": self.symbols_var.get(),
            "numbers": self.numbers_var.get()
        }

class PasswordManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Manager")
        self.root.geometry("600x450")
        self.root.resizable(False, False)
        self.password_manager = PasswordManager()
        self.password_generator = PasswordGenerator()

        tk.Button(root, text="Add Password", width=25, command=self.add_password).pack(pady=5)
        tk.Button(root, text="Retrieve Password", width=25, command=self.retrieve_password).pack(pady=5)
        tk.Button(root, text="Delete Password", width=25, command=self.delete_password).pack(pady=5)
        tk.Button(root, text="Generate Password", width=25, command=self.generate_password).pack(pady=5)
        tk.Button(root, text="Exit", width=25, command=root.quit).pack(pady=5)

    def add_password(self):
        dialog = AddPasswordDialog(self.root, title="Add Password")
        result = dialog.result
        if not result or not result["site"] or not result["password"]:
            return
        self.password_manager.add_password(result["site"], result["password"])
        messagebox.showinfo("Success", f"Password for {result['site']} added.")

    def retrieve_password(self):
        dialog = RetrievePasswordDialog(self.root, title="Retrieve Password")
        site = dialog.result
        if not site:
            return
        password = self.password_manager.retrieve_password(site)
        if password:
            messagebox.showinfo("Password Retrieved", f"Password for {site}: {password}")
        else:
            messagebox.showwarning("Not Found", f"No password found for {site}.")

    def delete_password(self):
        dialog = DeletePasswordDialog(self.root, title="Delete Password")
        site = dialog.result
        if not site:
            return
        self.password_manager.delete_password(site)
        messagebox.showinfo("Deleted", f"Password for {site} deleted.")

    def generate_password(self):
        dialog = GeneratePasswordDialog(self.root, title="Generate Password")
        result = dialog.result
        if not result:
            return
        length = result["length"]
        include_symbols = result["symbols"]
        include_numbers = result["numbers"]
        new_password = self.password_generator.generate_password(length, include_symbols, include_numbers)
        messagebox.showinfo("Generated Password", f"Generated Password: {new_password}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordManagerApp(root)
    root.mainloop()