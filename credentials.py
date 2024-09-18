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


def get_credentials():
    username, password = load_credentials()
    if not username or not password:
        root = tk.Tk()
        root.withdraw()
        username = simpledialog.askstring("Account", "Account:")
        password = simpledialog.askstring("Password", "Password:", show='*')
        save_credentials(username, password)
    return username, password
