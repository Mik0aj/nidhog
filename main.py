import cv2
import numpy as np
from PIL import ImageGrab
import subprocess
import os
from datetime import datetime
import time
from pynput.keyboard import Key, Listener
from queue import Queue
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
import src.game_state as gs

# Set the name of the target application window
GAME_NAME = "Nidhogg"
key_press_queue = Queue()

def get_window_position(name):
    # Use xdotool to search for the window and get its position and size
    cmd = ['xdotool', 'search', '--onlyvisible', '--name', name]
    window_info = subprocess.check_output(cmd).decode('utf-8').strip().split('\n')

    if len(window_info) == 0:
        return None
    
    # Get the window ID
    window_id = window_info[0]

    # Use xwininfo to get the position and size of the window
    cmd = ['xwininfo', '-id', window_id]
    win_info = subprocess.check_output(cmd).decode('utf-8')

    # Split the output of xwininfo on colons
    win_info_lines = win_info.split('\n')

    # Initialize variables for position and size
    x, y, width, height = None, None, None, None

    # Iterate over the lines and extract position and size
    for line in win_info_lines:
        if 'Absolute upper-left X' in line:
            x = int(line.split(':')[-1].strip())
        elif 'Absolute upper-left Y' in line:
            y = int(line.split(':')[-1].strip())
        elif 'Width' in line:
            width = int(line.split(':')[-1].strip())
        elif 'Height' in line:
            height = int(line.split(':')[-1].strip())

    if x is not None and y is not None and width is not None and height is not None:
        return x, y, width, height
    else:
        return None

def capture_game_screen():
    # Get the position and size of the game window
    window_pos = get_window_position(GAME_NAME)

    if window_pos is None:
        print("Game window not found!")
        return

    x, y, width, height = window_pos

    # Create a folder named 'screens' if it doesn't exist
    screens_folder = 'screens'
    if not os.path.exists(screens_folder):
        os.makedirs(screens_folder)

    # Calculate the time between each iteration for 60 Hz refresh rate
    iteration_time = 1 / 24  # 1 second divided by 60 (60 Hz)

    state_machine = gs.GameStateMachine()
    while True:
        # Record the start time of the iteration
        start_time = time.time()

        # Capture the specified window
        screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height))

        # Convert the screenshot to OpenCV format (numpy array) and convert to BGR color space
        frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)


        # Example of processing a video frame
        state_machine.update_state(frame)

        # Print the current state
        print(state_machine.get_current_state())
        # Generate timestamp for the screenshot
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')[:-4]



        # Save the captured frame with metadata
        filename = os.path.join(screens_folder, f'screenshot_{timestamp}.jpg')
        #cv2.imwrite(filename, frame)

        # Display the captured frame with metadata
        cv2.imshow('Captured Frame', frame)
        
        # Press 'q' to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # Calculate the time taken for this iteration
        iteration_duration = time.time() - start_time

        # If the iteration took less time than the desired refresh rate, wait for the remaining time
        if iteration_duration < iteration_time:
            time.sleep(iteration_time - iteration_duration)

    # Release the capture
    cv2.destroyAllWindows()

def save_screenshot_with_metadata(frame):
    # Get the timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')[:-4]

    # Process the key press queue to find the closest key press timestamp
    closest_key_press = None
    min_diff = float('inf')
    for key_press_timestamp in key_press_queue.queue:
        time_diff = datetime.now() - key_press_timestamp
        if time_diff.total_seconds() < min_diff:
            min_diff = time_diff.total_seconds()
            closest_key_press = key_press_timestamp

    # If there was a recent key press, include it in the filename
    if closest_key_press:
        keys_pressed = [closest_key_press.strftime('%Y-%m-%d_%H-%M-%S')]
    else:
        keys_pressed = []

    # Convert keys pressed into a string
    keys_str = '_'.join(keys_pressed)

    # Save the screenshot with metadata
    filename = os.path.join('screens', f'screenshot_{timestamp}_{keys_str}.jpg')
    cv2.imwrite(filename, frame)


def on_press(key):
    """Callback function for key press event."""
    print(f'{key} pressed.')
    # Capture the timestamp of the key press
    key_press_queue.put(datetime.now())

def on_release(key):
    """Callback function for key release event."""
    if key == Key.esc:
        # Stop listener
        return False

def main():
    # Start listening for key presses
    with Listener(on_press=on_press, on_release=on_release) as listener:
        while True:
            # Capture the game screen
            frame = capture_game_screen()

            # Check if there are any timestamps in the queue
            keys_pressed = []
            while not key_press_queue.empty():
                key = key_press_queue.get()
                keys_pressed.append(key)

            # Save the screenshot with metadata
            save_screenshot_with_metadata(frame, keys_pressed)

            # Check if the listener has stopped
            if listener.is_stopped:
                break


if __name__ == "__main__":
    main()
