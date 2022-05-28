from game.image import open, change, close
from game.level import start
import game.sound as s
import game.image.__init__


def draw_game():
    open.open()
    change.change()
    close.close()


draw_game()
start.start()
