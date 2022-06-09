from game.casting.actor import Actor
from game.shared.color import Color
from game.shared.point import Point
import random

ROCK = chr(219)
GEM = chr(42)
ROCK_POINT = -1
GEM_POINT = 1

class Artifact(Actor):
    """
    An item of cultural or historical interest. 
    
    The responsibility of an Artifact is to provide a message about itself.

    Attributes:
        _message (string): A short description about the artifact.
    """
    def __init__(self, COLS, ROWS, CELL_SIZE, FONT_SIZE):
        super().__init__()
        self._message = ""

        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        # y = -1
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)

        self.set_text(random.choice([ROCK, GEM]))
        self.set_font_size(FONT_SIZE)
        self.set_color(color)
        self.set_position(position)

        if self._text is ROCK:
            self.set_points(ROCK_POINT)
        if self._text is GEM:
            self.set_points(GEM_POINT)

        
    # def get_message(self):
    #     """Gets the artifact's message.
        
    #     Returns:
    #         string: The message.
    #     """
    #     return self._message
    
    # def set_message(self, message):
    #     """Updates the message to the given one.
        
    #     Args:
    #         message (string): The given message.
    #     """
    #     self._message = message