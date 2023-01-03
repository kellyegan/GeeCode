from geecode import Command


class Sequence:
    def __init__(self):
        self._commands = []

    def cmd(self, command_code, **parameters):
        command = Command(command_code, **parameters)
        self._commands.append(command.generate)

    def sub(self, sub_sequence):
        self._commands.append(sub_sequence.generate)

    def generate(self, include_comments=True, comment_indent=35, **parameters):
        gcode = "\n".join([c(comment_indent=comment_indent, include_comments=include_comments) for c in self._commands])
        return gcode
