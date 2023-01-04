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

    def test_command_generator(self):
        """Test generating a command with its own parameters"""
        g = Command.create_command("G1", x=15, y=10, z="_", comment="This is a test.")
        self.assertIsInstance(g, types.FunctionType)
        self.assertEqual("G1 X15 Y10 Z5                      ; This is a test.", g(z=5))
        self.assertEqual("G1 X5 Y10 Z25                      ; This is a test.", g(x=5, z=25))
        self.assertEqual("G1 X15 Y10 Z7.125", g(z=7.125, comments=False))
