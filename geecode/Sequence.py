from geecode import Command


class Sequence:
    def __init__(self):
        self._commands = []

    def cmd(self, command_code, comment=None, **parameters):
        """
        Add a command to the sequence
        :param command_code: G-code command to execute
        :param comment: Any comment to add to the command
        :param parameters: key-value parameters representing g-code commands parameters
        :return:
        """
        command = Command(command_code, comment=comment, **parameters)
        self._commands.append(command.generate)

    def sub(self, sub_sequence):
        """
        Add a sub-sequence to this sequence
        :param Sequence sub_sequence:
        :return:
        """
        self._commands.append(sub_sequence.generate)

    def generate(self, comments=True, indent=35):
        """
        Generate gcode for this sequence
        :param comments: Boolean to sets whether comments are included
        :param indent: Number of spaces the comment is justified from command.
        :param parameters: Any parameters for this command
        :return: gcode string
        """
        gcode = "\n".join([c(comments=comments, indent=indent) for c in self._commands])
        return gcode
