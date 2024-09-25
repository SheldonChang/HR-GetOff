import os
import json
import tkinter as tk
from tkinter import simpledialog

CREDENTIALS_FILE = 'credentials.json'


def save_credentials(username, password):
    credentials = {'username': username, 'password': password}
    with open(CREDENTIALS_FILE, 'w') as file:
        json.dump(credentials, file)


def load_credentials():
    if os.path.exists(CREDENTIALS_FILE):
        with open(CREDENTIALS_FILE, 'r') as file:
            credentials = json.load(file)
            return credentials['username'], credentials['password']
    return None, None


class CredentialsDialog(simpledialog.Dialog):
    def body(self, master):
        # Username label with emoji
        self.id_label = tk.Label(master, text="ID: ")
        self.id_label.grid(row=0, column=0, padx=5, pady=5)

        # Username entry
        self.id_entry = tk.Entry(master)
        self.id_entry.grid(row=0, column=1, padx=5, pady=5)

        # Password label with emoji
        self.pw_label = tk.Label(master, text="PW:")
        self.pw_label.grid(row=1, column=0, padx=5, pady=5)

        # Password entry
        self.pw_entry = tk.Entry(master, show='*')
        self.pw_entry.grid(row=1, column=1, padx=5, pady=5)

    def apply(self):
        self.result = (self.id_entry.get(), self.pw_entry.get())


def get_credentials():
    username, password = load_credentials()
    if not username or not password:
        root = tk.Tk()
        root.withdraw()
        dialog = CredentialsDialog(root)
        username, password = dialog.result if dialog.result else (None, None)

        if username and password:
            save_credentials(username, password)
    return username, password
