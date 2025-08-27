# src/auth.py
from instagrapi import Client
import config
import helpers as Helper
import os

SESSION_FILE = "session.json"

def login():
    """Login function using session.json if available"""
    print("   Initializing login...")
    api = Client()
    api.delay_range = [5, 10]
    Helper.load_all_config()

    if os.path.exists(SESSION_FILE):
        print("   Logging with previous session...")
        api.load_settings(SESSION_FILE)
        api.login(config.USERNAME, config.PASSWORD)
        api.dump_settings(SESSION_FILE)
        api.get_timeline_feed()
        print("   Logged in successfully.")
        return api
    else:
        print("   Logging with username and password...")
        api.login(config.USERNAME, config.PASSWORD)
        api.dump_settings(SESSION_FILE)
        api.get_timeline_feed()
        print("   Logged in successfully.")
        return api