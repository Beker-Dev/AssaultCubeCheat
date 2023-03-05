from core.cheat import Cheat
from ui.cheat_ui import CheatUI
import json
from utils import get_settings
import threading


if __name__ == '__main__':
    settings = get_settings()
    cheat = Cheat(settings=settings)
    cheat_ui = CheatUI(title='Assault Cube Cheat - Made By Beker', settings=settings, cheat=cheat)

    cheat_ui_thread = threading.Thread(target=cheat_ui.run)
    cheat_ui_thread.start()
    cheat.run()
