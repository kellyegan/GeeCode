

class Parser:
    def __init__(self, input_file=None):
        if isinstance(input_file, str):
            print(input_file)
        elif input_file is not None:
            print("Probably a file?")
        pass

    def __enter__(self):
        pass

    def __exit__(self):
        pass


if __name__ == '__main__':
    p = Parser(input_file="../tests/sample.gcode")
