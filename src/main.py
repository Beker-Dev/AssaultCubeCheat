from ui.cheat_ui import CheatUI
from core.cheat import Cheat
import json
from utils import get_settings

if __name__ == '__main__':
    settings = get_settings()

    cheat_ui = CheatUI(title='Assault Cube Cheat - Made By Beker', settings=settings)
    cheat = Cheat(settings=settings)

    cheat_ui.run()

    while 1:
        cheat.run()
