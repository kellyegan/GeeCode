from geecode import Command

class Sequence:
    def __init__(self):
        self._commands = []

    def cmd(self, command_code, **parameters):
        command = Command(command_code, **parameters)
        self._commands.append(command)

    def generate(self):
        gcode = "\n".join([c.generate().strip() for c in self._commands])
        print(gcode)
        return gcode
