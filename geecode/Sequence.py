from geecode import Command


class Sequence:
    def __init__(self):
        self._commands = []

    def cmd(self, command_code, **parameters):
        command = Command(command_code, **parameters)
        self._commands.append(command)

    def generate(self, include_comments=True, comment_indent=35):
        gcode = ""
        for command in self._commands:
            if isinstance(command, Command):
                gcode += command.generate(comment_indent=comment_indent, include_comments=include_comments) + "\n"
        return gcode
