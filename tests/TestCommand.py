import types
import unittest
from geecode import Command


class TestCommand(unittest.TestCase):
    def test_no_params(self):
        """Test a command without parameters"""
        c = Command("G28")
        self.assertEqual(c.generate(), 'G28')

    def test_params(self):
        """Test a command with parameters"""
        c = Command("G1", x=15, y=10)
        self.assertEqual("G1 X15 Y10", c.generate())

    def test_comments_no_params(self):
        """Test a command comments and no parameters"""
        c = Command("G80", comment="mesh bed leveling")
        self.assertEqual("G80                                ; mesh bed leveling", c.generate())

    def test_comments_params(self):
        """Test a command with comments and parameters"""
        c = Command("M201", p=9000, y=9000, z=500, e=10000, comment="sets max accelerations")
        self.assertEqual("M201 P9000 Y9000 Z500 E10000       ; sets max accelerations", c.generate())

    def test_comment_only(self):
        """Test a command that is only a comment"""
        c = Command(comment="sets max accelerations")
        self.assertEqual("; sets max accelerations", c.generate())

    def test_blank(self):
        """Test a blank command"""
        c = Command()
        self.assertEqual("", c.generate())

    def test_decimal_params(self):
        """Test formmating of decimal numbers in parameters"""
        c = Command("G1", x=15.123516156, y=0.456, z=0.387601, e=0.000004932)
        self.assertEqual("G1 X15.12352 Y0.456 Z0.3876 E0", c.generate())

    def test_variable(self):
        """Test a command with comments and parameters"""
        c = Command("G1", x=40, y=50.5, z=0.5, e="{e_value}", comment="sets max accelerations")
        generated_gcode = c.generate(e_value=0.1)
        self.assertEqual("G1 X40 Y50.5 Z0.5 E0.1             ; sets max accelerations",generated_gcode)