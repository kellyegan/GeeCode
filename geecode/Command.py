
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


class Command:
    """
    Object for containing a single g-code command
    """

    def __init__(self, code=None, comment=None, **parameters):
        self.code = code
        self.parameters = parameters
        self.comment = comment

    def generate(self, comments=True, indent=35, **variables):
        """
        Generate a line of g-code from the command object
        :param comments: Include comments in output
        :param indent: Number of spaces to indent the comment
        :return: string representing code command
        """

        template = template_gcode(code=self.code, **self.parameters)
        gcode = template

        if self.comment is not None and comments:
            gcode = f'{gcode.format(**variables).ljust(indent - 1)} ; {self.comment.format(**variables)}'

        return gcode.strip()



