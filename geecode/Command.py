
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


