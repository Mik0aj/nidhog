import os
import unittest
import cv2
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
import src.game_state as game_state

# Directory of the script
SCRIPT_DIR = os.path.dirname((os.path.abspath(__file__)))
RESOURCE_DIR = os.path.join(SCRIPT_DIR, 'resources')

EXAMPLE_CREDIT = os.path.join(RESOURCE_DIR, 'credits.jpg')
EXAMPLE_HOW_TO_PLAY = os.path.join(RESOURCE_DIR, 'how_to_play.jpg')
EXAMPLE_MULTIPLAYER = os.path.join(RESOURCE_DIR, 'multiplayer.jpg')
EXAMPLE_OPTIONS = os.path.join(RESOURCE_DIR, 'options.jpg')
EXAMPLE_PRESS_START = os.path.join(RESOURCE_DIR, 'press_start.jpg')
EXAMPLE_QUIT_TO_DESKTOP = os.path.join(RESOURCE_DIR, 'quit_to_desktop.jpg')
EXAMPLE_SINGLE_PLAYER = os.path.join(RESOURCE_DIR, 'single_player.jpg')
EXAMPLE_TOURNAMENT = os.path.join(RESOURCE_DIR, 'tournament.jpg')

EXAMPLE_GO_LEFT = os.path.join(RESOURCE_DIR, 'go_left.jpg')
EXAMPLE_GO_RIGHT = os.path.join(RESOURCE_DIR, 'go_right.jpg')
EXAMPLE_SINGLE_PLAYER_BEGIN = os.path.join(RESOURCE_DIR, 'single_player_begin.jpg')
EXAMPLE_SINGLE_PLAYER_BEGIN_TWO = os.path.join(RESOURCE_DIR, 'single_player_begin_two.jpg')

class TestCheckIfAllPixelsWhite(unittest.TestCase):
    
    def test_check_if_all_pixels_white_for_credit(self):
        image = cv2.imread(EXAMPLE_CREDIT)
        mask = cv2.imread(game_state.CREDIT_MASK)
        result = game_state.check_if_all_pixels_white(image, mask, 165)
        self.assertTrue(result, "Expected result to be True")

    def test_check_if_all_pixels_white_for_how_to_play(self):
        image = cv2.imread(EXAMPLE_HOW_TO_PLAY)
        mask = cv2.imread(game_state.HOW_TO_PLAY_MASK)
        result = game_state.check_if_all_pixels_white(image, mask, 165)
        self.assertTrue(result, "Expected result to be True")

    def test_check_if_all_pixels_white_for_multiplayer(self):
        image = cv2.imread(EXAMPLE_MULTIPLAYER)
        mask = cv2.imread(game_state.MULTIPLAYER_MASK)
        result = game_state.check_if_all_pixels_white(image, mask, 165)
        self.assertTrue(result, "Expected result to be True")

    def test_check_if_all_pixels_white_for_options(self):
        image = cv2.imread(EXAMPLE_OPTIONS)
        mask = cv2.imread(game_state.OPTIONS_MASK)
        result = game_state.check_if_all_pixels_white(image, mask, 165)
        self.assertTrue(result, "Expected result to be True")

    def test_check_if_all_pixels_white_for_press_start(self):
        image = cv2.imread(EXAMPLE_PRESS_START)
        mask = cv2.imread(game_state.PRESS_START_MASK)
        result = game_state.check_if_all_pixels_white(image, mask, 165)
        self.assertTrue(result, "Expected result to be True")

    def test_check_if_all_pixels_white_for_quit_to_the_desktop(self):
        image = cv2.imread(EXAMPLE_QUIT_TO_DESKTOP)
        mask = cv2.imread(game_state.QUIT_TO_DESKTOP_MASK)
        result = game_state.check_if_all_pixels_white(image, mask, 165)
        self.assertTrue(result, "Expected result to be True")

    def test_check_if_all_pixels_white_for_single_player(self):
        image = cv2.imread(EXAMPLE_SINGLE_PLAYER)
        mask = cv2.imread(game_state.SINGLE_PLAYER_MASK)
        result = game_state.check_if_all_pixels_white(image, mask, 165)
        self.assertTrue(result, "Expected result to be True")

    def test_check_if_all_pixels_white_for_tournament(self):
        image = cv2.imread(EXAMPLE_TOURNAMENT)
        mask = cv2.imread(game_state.TOURNAMENT_MASK)
        result = game_state.check_if_all_pixels_white(image, mask, 165)
        self.assertTrue(result, "Expected result to be True")

    def test_check_if_all_pixels_white_for_go_left(self):
        image = cv2.imread(EXAMPLE_GO_LEFT)
        mask = cv2.imread(game_state.GO_LEFT_MASK)
        result = game_state.check_if_all_pixels_white(image, mask, 165)
        self.assertTrue(result, "Expected result to be True")

    def test_check_if_all_pixels_white_for_go_right(self):
        image = cv2.imread(EXAMPLE_GO_RIGHT)
        mask = cv2.imread(game_state.GO_RIGHT_MASK)
        result = game_state.check_if_all_pixels_white(image, mask, 165)
        self.assertTrue(result, "Expected result to be True")

    def test_check_if_all_pixels_white_for_single_player_begin(self):
        image = cv2.imread(EXAMPLE_SINGLE_PLAYER_BEGIN)
        mask = cv2.imread(game_state.SINGLE_PLAYER_BEGIN_MASK)

        result = game_state.check_if_all_pixels_white(image, mask, 165)
        self.assertTrue(result, "Expected result to be True")

    def test_check_if_all_pixels_white_for_single_player_begin_two(self):
        image = cv2.imread(EXAMPLE_SINGLE_PLAYER_BEGIN_TWO)
        mask = cv2.imread(game_state.SINGLE_PLAYER_BEGIN_MASK_TWO)
        result = game_state.check_if_all_pixels_white(image, mask, 165)
        self.assertTrue(result, "Expected result to be True")


if __name__ == '__main__':
    unittest.main()
