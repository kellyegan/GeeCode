import types
import unittest
from geecode import Command


class TestCommand(unittest.TestCase):
    def test_no_params(self):
        """Should print a command without any parameters or comments"""
        c = Command("G28")
        self.assertEqual(c.generate(), 'G28')

    def test_params(self):
        """Should print a command with parameters"""
        c = Command("G1", x=15, y=10)
        self.assertEqual("G1 X15 Y10", c.generate())

    def test_comments_no_params(self):
        """Should print a command without parameters and print indented comment"""
        c = Command("G80", comment="mesh bed leveling")
        self.assertEqual("G80                                ; mesh bed leveling", c.generate())

    def test_comments_params(self):
        """Should print command and properly indented comment"""
        c = Command("M201", p=9000, y=9000, z=500, e=10000, comment="sets max accelerations")
        self.assertEqual("M201 P9000 Y9000 Z500 E10000       ; sets max accelerations", c.generate())

    def test_comment_only(self):
        """Should print a comment without command or indent"""
        c = Command(comment="sets max accelerations")
        self.assertEqual("; sets max accelerations", c.generate())

    def test_none_value(self):
        """Should ignore parameter completely"""
        c = Command("G1", x=10, y=20, z=None)
        self.assertEqual("G1 X10 Y20", c.generate())

    def test_empty_value(self):
        """Should print just key without any value. Used for flag parameters"""
        c = Command("G1", x=10, y=20, z="")
        self.assertEqual("G1 X10 Y20 Z", c.generate())

    def test_blank(self):
        """Should return an empty string"""
        c = Command()
        self.assertEqual("", c.generate())

    def test_decimal_params(self):
        """Should print properly formated decimal without trailing zeros"""
        c = Command("G1", x=15.123516156, y=0.456, z=0.387601, e=0.000004932)
        self.assertEqual("G1 X15.12352 Y0.456 Z0.3876 E0", c.generate())

    def test_variable(self):
        """Should print command with a variable that is assignable at time of generation"""
        c = Command("G1", x=40, y=50.5, z=0.5, e="{e_value}", comment="sets max accelerations")
        generated_gcode = c.generate(e_value=0.1)
        self.assertEqual("G1 X40 Y50.5 Z0.5 E0.1             ; sets max accelerations",generated_gcode)