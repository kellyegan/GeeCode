from geecode import Command


class Sequence:
    def __init__(self):
        self._commands = []

    def cmd(self, command_code, **parameters):
        command = Command(command_code, **parameters)
        self._commands.append(command)

    def generate(self, comment_indent=35):
        gcode = "\n".join([c.generate(comment_indent=comment_indent).strip() for c in self._commands])
        return gcode
