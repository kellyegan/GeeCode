from string import Template


class Sequence:
    """ Class to hold a sequence of g-code commands"""
    def __init__(self):
        self._commands = []

    def cmd(self, command_code, comment=None, **parameters):
        """ Add a command to the sequence """
        command = create_command(command_code, comment=comment, **parameters)
        self._commands.append(command)

    def move(self, comment=None, x=None, y=None, z=None, e=None, f=None):
        """ Use G1 command to move along one or more axes.  """
        self.cmd("G1", comment=comment, x=x, y=y, z=z, e=e, f=f)

    def sub(self, sub_sequence, **variables):
        """ Add a sub-sequence to the current sequence """

        def generate(comments=True, indent=35):
            return sub_sequence.generate(comments=comments, indent=indent, **variables)

        self._commands.append(generate)

    def generate(self, comments=True, indent=35, **variables):
        """ Generate gcode for sequence """

        gcode = []
        for c in self._commands:
            new_cmd = c(comments=comments, indent=indent, **variables)
            if type(new_cmd) == list:
                gcode.extend(new_cmd)
            else:
                gcode.append(new_cmd)
        return gcode


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
        formatted_variables = {k: format_value(v) for k, v in variables.items()}
        template = Template(template_gcode(code=code, **parameters))
        gcode = template.safe_substitute(**formatted_variables)

        if comment is not None and comments:
            gcode = f'{gcode.ljust(indent - 1)} ; {comment.format(**variables)}'
        return gcode.strip()

    return command



