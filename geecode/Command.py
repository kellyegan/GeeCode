def format_num(number):
    """
    Formats numbers for parameters with up to 5 decimal places but strips trailing zeros
    :param number:
    :return:
    """
    number_string = f"{number:0.5f}" if not isinstance(number, str) else ""
    return number_string.rstrip('0').rstrip('.')


class Command:
    """
    Object for containing a single g-code command
    """
    def __init__(self, command_code=None, **parameters):
        self.command = command_code
        self.comment = parameters.pop("comment", None)
        self.parameters = parameters

    def __eq__(self, other):
        if not isinstance(other, Command):
            return False
        if self.command != other.command:
            return False
        if self.comment != other.comment:
            return False
        if self.parameters != other.parameters:
            return False
        return True

    def generate(self, include_comments=True, comment_indent=35):
        """
        Generate a line of g-code from the command object
        :param include_comments: Include comments in output
        :param comment_indent: Number of spaces to indent the comment
        :return: string representing code command
        """
        gcode = ""

        if self.command is not None:
            parameters_list = [f"{k.upper().strip()}{format_num(v)}" for k, v in self.parameters.items()]
            gcode += f'{self.command.upper()} {" ".join(parameters_list)} '

        if self.comment is not None and include_comments:
            gcode = f'{gcode.ljust(comment_indent - 1)} ; {self.comment}'

        return gcode.strip()

