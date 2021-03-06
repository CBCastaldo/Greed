from game.casting.actor import Actor
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Catch the Gems"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 40

def main():
    
    # create the cast
    cast = Cast()
    
    # create the banner
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE + 7)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    # create the robot
    x = int(MAX_X / 2)
    # y = int(MAX_Y / -10)
    y = MAX_Y - CELL_SIZE
    position = Point(x, y)

    catcher = Actor()
    catcher.set_text("#")
    catcher.set_font_size(FONT_SIZE)
    catcher.set_color(WHITE)
    catcher.set_position(position)
    cast.add_actor("catchers", catcher)

    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service, DEFAULT_ARTIFACTS, COLS, ROWS, FONT_SIZE, CELL_SIZE)
    director.start_game(cast)


if __name__ == "__main__":
    main()