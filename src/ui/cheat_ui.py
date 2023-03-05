import os
import termcolor
from core.cheat import Cheat

class CheatUI:
    def __init__(self, title: str, settings: dict, cheat: Cheat):
        self.title = title.title().strip()
        self.spacing = len(title) + 50
        self.settings = settings

    def menu(self):
        self.clean_screen()
        self.fill_spacing()
        self.show_title()
        self.fill_spacing()
        self.show_settings()
        self.show_status()

    def fill_spacing(self, char: str = '-'):
        print(char * self.spacing)

    def show_title(self):
        print(f'{self.title:^{self.spacing}}')

    def show_status(self, status: str = 'Running'):
        print('\n')
        print('>'*5, end=' ')
        print(f'Cheat Status:', status)

    def show_settings(self):
        for k, v in self.settings.items():
            name = k.title()
            turned_on = 'ON' if v.get("on") else 'OFF'
            text_color = 'green' if v.get("on") else 'red'
            print(f'{name::<15} [{termcolor.colored(turned_on, text_color)}]')

    def clean_screen(self):
        os.system('cls')

    def get_command(self):
        cmd = input('?: ').strip()
        if cmd.startswith('/'):
            cmd = cmd[1:]
            if cmd in self.settings:
                conf_value = self.settings[cmd]
                conf_value['on'] = not conf_value['on']
                self.settings[cmd] = conf_value
                text_color = 'green' if conf_value.get("on") else 'red'
                turned_on = 'ON' if conf_value.get("on") else 'OFF'
                print(f'Ok: {self.settings[cmd]} set to [{termcolor.colored(turned_on, text_color)}]')
                self.menu()
                return
        termcolor.cprint('Error: Command not found', 'red')

    def run(self):
        self.menu()
        while 1:
            self.get_command()

