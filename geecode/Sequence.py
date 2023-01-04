from geecode import Command


class Sequence:
    def __init__(self):
        self._commands = []

    def cmd(self, command_code, **parameters):
        """
        Add a command to the sequence
        :param command_code: G-code command to execute
        :param parameters: key-value parameters representing g-code commands parameters
        :return:
        """
        command = Command(command_code, **parameters)
        self._commands.append(command.generate)

    def sub(self, sub_sequence):
        """
        Add a sub-sequence to this sequence
        :param Sequence sub_sequence:
        :return:
        """
        self._commands.append(sub_sequence.generate)

    def generate(self, comments=True, comment_indent=35, **parameters):
        """
        Generate gcode for this sequence
        :param comments: Boolean to sets whether comments are included
        :param comment_indent: Number of spaces the comment is justified from command.
        :param parameters: Any parameters for this command
        :return: gcode string
        """
        gcode = "\n".join([c(comment_indent=comment_indent, comments=comments) for c in self._commands])
        return gcode
