

class Parser:
    def __init__(self, input_file=None, encoding="locale"):
        if isinstance(input_file, str):
            self.input_file = open(input_file, "r", encoding=encoding)
        elif input_file is not None:
            self.input_file = input_file
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        self.input_file.close()
