import os
import cv2
import numpy as np

# Directory of the script
SCRIPT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define paths for the mask files
CREDIT_MASK = os.path.join(SCRIPT_DIR, 'resources', 'masks', 'mask_credits.png')
HOW_TO_PLAY_MASK = os.path.join(SCRIPT_DIR, 'resources', 'masks', 'mask_how_to_play.png')
MULTIPLAYER_MASK = os.path.join(SCRIPT_DIR, 'resources', 'masks', 'mask_multiplayer.png')
OPTIONS_MASK = os.path.join(SCRIPT_DIR, 'resources', 'masks', 'mask_options.png')
SINGLE_PLAYER_BEGIN_MASK = os.path.join(SCRIPT_DIR, 'resources', 'masks', 'mask_single_player_begin.png')
SINGLE_PLAYER_BEGIN_MASK_TWO = os.path.join(SCRIPT_DIR, 'resources', 'masks', 'mask_single_player_begin_two.png')
TOURNAMENT_MASK = os.path.join(SCRIPT_DIR, 'resources', 'masks', 'mask_tournament.png')
GO_LEFT_MASK = os.path.join(SCRIPT_DIR, 'resources', 'masks', 'mask_go_left.png')
GO_RIGHT_MASK = os.path.join(SCRIPT_DIR, 'resources', 'masks', 'mask_go_right.png')
PRESS_START_MASK = os.path.join(SCRIPT_DIR, 'resources', 'masks', 'mask_press_start.png')
QUIT_TO_DESKTOP_MASK = os.path.join(SCRIPT_DIR, 'resources', 'masks', 'mask_quit_to_desktop.png')
SINGLE_PLAYER_MASK = os.path.join(SCRIPT_DIR, 'resources', 'masks', 'mask_single_player.png')

OUTPUT_IMAGE = os.path.join(SCRIPT_DIR, 'masked_image.jpg')

class GameState:
    CREDITS = "Credits"
    HOW_TO_PLAY = "HowToPlay"
    MULTIPLAYER = "Multiplayer"
    OPTIONS = "Options"
    SINGLE_PLAYER_BEGIN = "SinglePlayerBegin"
    SINGLE_PLAYER_BEGIN_TWO = "SinglePlayerBeginTwo"
    TOURNAMENT = "Tournament"
    GO_LEFT = "GoLeft"
    GO_RIGHT = "GoRight"
    PRESS_START = "PressStart"
    QUIT_TO_DESKTOP = "QuitToDesktop"
    SINGLE_PLAYER = "SinglePlayer"

import cv2
import numpy as np

import cv2
import numpy as np

def check_if_all_pixels_white(image, mask, threshold=245, mode='average'):
    """
    Checks if all pixels in the masked region of an image are white.

    Parameters:
    - image: A numpy array representing the image.
    - mask: A numpy array representing the mask.
    - threshold: An integer representing the threshold value for a pixel to be considered white.
    - mode: A string indicating the mode to use for the check ('average' or 'min').

    Returns:
    - True if all pixels in the masked region are white, False otherwise.
    """
    # Ensure the mask is in the correct format (grayscale)
    if len(mask.shape) == 3:
        mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    
    # Ensure the mask is binary (black and white)
    _, mask = cv2.threshold(mask, 128, 255, cv2.THRESH_BINARY)

    # Perform bitwise AND operation to apply the mask
    masked_image = cv2.bitwise_and(image, image, mask=mask)

    # Ensure the masked_image is in the correct format (grayscale)
    if len(masked_image.shape) == 3:
        masked_image = cv2.cvtColor(masked_image, cv2.COLOR_BGR2GRAY)

    # Create a boolean mask where True indicates pixels within the masked region
    masked_region = mask != 0

    if mode == 'average':
        # Use the average pixel value in the masked region
        value = np.mean(masked_image[masked_region])
    elif mode == 'min':
        # Use the lowest pixel value in the masked region
        value = np.min(masked_image[masked_region])
    else:
        raise ValueError("Invalid mode specified. Mode must be either 'average' or 'min'.")
    # print(f"Value used for check: {value}")
    # # Display the image
    # cv2.imshow('Masked Image', masked_image)
    # cv2.waitKey(0) # Wait for a key press to close the window
    # cv2.destroyAllWindows()
    # Check if all pixels in the masked region are white
    is_white = value >= threshold
    return is_white



def load_image_grayscale(file_path):
    image = cv2.imread(file_path)
    if image is None:
        raise FileNotFoundError(f"Image not found at {file_path}")
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

class GameStateMachine:
    def __init__(self):
        self.current_state = None
        # Define the masks as class attributes for easy access
        self.masks = {
            GameState.CREDITS: load_image_grayscale(CREDIT_MASK),
            GameState.HOW_TO_PLAY: load_image_grayscale(HOW_TO_PLAY_MASK),
            GameState.MULTIPLAYER: load_image_grayscale(MULTIPLAYER_MASK),
            GameState.OPTIONS: load_image_grayscale(OPTIONS_MASK),
            GameState.SINGLE_PLAYER_BEGIN: load_image_grayscale(SINGLE_PLAYER_BEGIN_MASK),
            GameState.SINGLE_PLAYER_BEGIN_TWO: load_image_grayscale(SINGLE_PLAYER_BEGIN_MASK_TWO),
            GameState.TOURNAMENT: load_image_grayscale(TOURNAMENT_MASK),
            GameState.GO_LEFT: load_image_grayscale(GO_LEFT_MASK),
            GameState.GO_RIGHT: load_image_grayscale(GO_RIGHT_MASK),
            GameState.PRESS_START: load_image_grayscale(PRESS_START_MASK),
            GameState.QUIT_TO_DESKTOP: load_image_grayscale(QUIT_TO_DESKTOP_MASK),
            GameState.SINGLE_PLAYER: load_image_grayscale(SINGLE_PLAYER_MASK),
        }


    def update_state(self, frame):

        # Convert the frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Check each mask to determine the current state
        for state, mask in self.masks.items():
            if check_if_all_pixels_white(gray_frame, mask):
                self.current_state = state
                break

    def get_current_state(self):
        return self.current_state

if __name__ == '__main__':
    # Example usage
    # Load an image and a mask (assuming they are numpy arrays)
    image = cv2.imread('/home/mikoaj/Documents/nidhog/resources/tournament.jpg')
    mask = cv2.imread('/home/mikoaj/Documents/nidhog/resources/masks/mask_tournament.png', cv2.IMREAD_GRAYSCALE)

    # Check if all pixels in the masked image are white
    result = check_if_all_pixels_white(image, mask, 250)
    print("All pixels are white:", result)
