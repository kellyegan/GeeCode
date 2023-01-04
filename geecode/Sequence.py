import geecode


def format_value(value):
    number_string = f"{value:0.5f}" if not isinstance(value, str) else value
    return number_string.rstrip('0').rstrip('.')


def template_gcode(code=None, **parameters):
    if code is None:
        return ""

    template = code.upper()
    parameters_list = [k.upper() + format_value(v) for k, v in parameters.items() if v is not None]

    if len(parameters_list) > 0:
        template += " " + " ".join(parameters_list)

    return template


def create_command(code=None, comment=None, **parameters):

    def command(comments=True, indent=35, **variables):
        gcode = template_gcode(code=code, **parameters)

        if comment is not None and comments:
            gcode = f'{gcode.format(**variables).ljust(indent - 1)} ; {comment.format(**variables)}'

        return gcode.strip()

    return command


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
        command = create_command(command_code, comment=comment, **parameters)
        self._commands.append(command)

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


