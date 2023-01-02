def _format_num(number):
    return f"{number:0.5g}" if not isinstance(number, str) else ""


class Command:
    """
    Object for containing a single g-code command
    """
    def __init__(self, command_code, **parameters):
        self.command = command_code
        self.comment = parameters.pop("comment", None)
        self.parameters = parameters

    def generate(self, include_comments=True, comment_indent=35):
        """
        Generate a line of g-code from the command object
        :param include_comments: Include comments in output
        :param comment_indent: Number of spaces to indent the comment
        :return: string representing code command
        """
        gcode = ""

        if self.command != "":
            parameters_list = [f"{k.upper().strip()}{format_num(v)}" for k, v in self.parameters.items()]
            gcode += f'{self.command.upper()} {" ".join(parameters_list)} '

        if self.comment is not None:
            gcode += f'{gcode.ljust(comment_indent)} ; {self.comment}'

        return gcode.strip()

