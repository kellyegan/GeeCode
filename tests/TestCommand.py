import types
import unittest
from geecode.Sequence import create_command


class TestCommand(unittest.TestCase):
    def test_no_params(self):
        """Should print a g-code command without any parameters or comments"""
        c = create_command("G28")
        self.assertEqual(c(), 'G28')

    def test_params(self):
        """Should print a g-code command with parameters"""
        c = create_command("G1", x=15, y=10)
        self.assertEqual("G1 X15 Y10", c())

    def test_comments_no_params(self):
        """Should print a g-code command without parameters and print indented comment"""
        c = create_command("G80", comment="mesh bed leveling")
        self.assertEqual("G80                                ; mesh bed leveling", c())

    def test_comments_params(self):
        """Should print g-code command and properly indented comment"""
        c = create_command("M201", p=9000, y=9000, z=500, e=10000, comment="sets max accelerations")
        self.assertEqual("M201 P9000 Y9000 Z500 E10000       ; sets max accelerations", c())

    def test_comment_only(self):
        """Should print a comment without g-code command or indent"""
        c = create_command(comment="sets max accelerations")
        self.assertEqual("; sets max accelerations", c())

    def test_none_value(self):
        """Should ignore parameter completely"""
        c = create_command("G1", x=10, y=20, z=None)
        self.assertEqual("G1 X10 Y20", c())

    def test_empty_value(self):
        """Should print just key without any value. Used for flag parameters"""
        c = create_command("G1", x=10, y=20, z="")
        self.assertEqual("G1 X10 Y20 Z", c())

    def test_blank(self):
        """Should return an empty string"""
        c = create_command()
        self.assertEqual("", c())

    def test_decimal_params(self):
        """Should print properly formated decimal without trailing zeros"""
        c = create_command("G1", x=15.123516156, y=0.456, z=0.387601, e=0.000004932)
        self.assertEqual("G1 X15.12352 Y0.456 Z0.3876 E0", c())

    def test_variable(self):
        """Should print command with a variable that is assignable at time of generation"""
        c = create_command("G1", x=40, y=50.5, z=0.5, e="$e_value", comment="sets max accelerations")
        generated_gcode = c(e_value=0.1)
        self.assertEqual("G1 X40 Y50.5 Z0.5 E0.1             ; sets max accelerations", generated_gcode)