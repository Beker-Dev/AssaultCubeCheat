from ReadWriteMemory import ReadWriteMemory


class Cheat:
    def __init__(self, settings: dict):
        self.rwm = ReadWriteMemory()
        self.process = self.rwm.get_process_by_name('ac_client.exe')
        self.process.open()

        self.base_address = 0x00400000
        self.pointers = {
            'ammo': self.process.get_pointer(
                self.base_address+0x0017F110,
                offsets=[0x0, 0x140]
            ),
            'health': self.process.get_pointer(
                self.base_address+0x00183828,
                offsets=[0x8, 0x24, 0x64, 0x34, 0x98, 0x64, 0x36C]
            ),
            'grenade': self.process.get_pointer(
                self.base_address+0x0017F110,
                offsets=[0x0, 0x144]
            )
        }
        self.values = {
            'ammo': None,
            'health': None,
            'grenade': None
        }
        self.settings = settings

    def get_value_by_key(self, key):
        return self.process.read(self.pointers[key])

    def read_values(self):
        for k, v in self.pointers.items():
            self.values[k] = self.process.read(v)

    def write_values(self):
        for k, v in self.settings.items():
            if v.get('on'):
                self.values[k] = v.get('amount')
                self.process.write(self.pointers[k], self.values[k])

    def run(self):
        while 1:
            self.read_values()
            self.write_values()
