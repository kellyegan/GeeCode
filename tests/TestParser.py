import unittest
from geecode import Parser


class TestParser(unittest.TestCase):

    def test_createParserClose(self):
        """
        Create new Parser with input file and close it.
        """
        p = Parser("sample.gcode")
        p.close()

        f = open("sample.gcode")
        q = Parser(f)
        q.close()

    def test_withContext(self):
        """
        Test parser using with context to open file
        """
        with Parser("sample.gcode") as p:
            pass

