import unittest
from geecode import Parser


class TestParser(unittest.TestCase):
    def test_read_file(self):
        p = Parser("sample.gcode")
        pass
