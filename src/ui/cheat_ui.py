import os


class CheatUI:
    def __init__(self, title: str, settings: dict):
        self.title = title.title().strip()
        self.spacing = len(title) + 50
        self.settings = settings

    def menu(self):
        self.set_menu_color()
        self.clean_screen()
        self.fill_spacing()
        self.show_title()
        self.fill_spacing()
        self.show_settings()
        self.show_status()

    def set_menu_color(self, code: str = '0a'):
        os.system('color ' + code)

    def fill_spacing(self, char: str = '-'):
        print(char * self.spacing)

    def show_title(self):
        print(f'{self.title:^{self.spacing}}')

    def show_status(self, status: str = 'Em execução'):
        print('\n')
        print('>'*5, end=' ')
        print(f'Cheat Status:', status)

    def translation(self, key: str):
        key = key.lower()
        translator = {
            'grenade': 'Granada',
            'ammo': 'Munição',
            'health': 'Saúde'
        }
        return translator.get(key, key)

    def show_settings(self):
        print('Configurações - (Altere no arquivo "cheat_values.json" e reinicie o cheat):\n\n')
        for k, v in self.settings.items():
            name = self.translation(k).title()
            turned_on = 'Sim' if v.get("on") else 'Não'
            amount = v.get("amount")
            print(f'{name}:')
            print(f'\tLigado: {turned_on}')
            print(f'\tQuantidade: {amount}')

    def clean_screen(self):
        os.system('cls')

    def run(self):
        self.menu()

