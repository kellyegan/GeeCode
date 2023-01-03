import unittest
from geecode import Command
from geecode import Sequence


class TestSequence(unittest.TestCase):

    def setUp(self):
        self.s = Sequence()
        self.s.cmd("M73", p=0, r=0, comment="set print progress")
        self.s.cmd("M205", x=10, y=10, z=0.2, e=4.5, comment="sets the jerk limits, mm/sec")
        self.s.cmd("M207", comment="Fans off")

    def test_add_command(self):
        """Add a command to the sequence"""
        s = Sequence()
        c = Command("G1", x=15, y=16, e=0.05)
        s.cmd("G1", x=15, y=16, e=0.05)

        added_command = s._commands[0]
        self.assertEqual(len(s._commands), 1)
        self.assertIsInstance(added_command, Command)
        self.assertEqual(added_command, c)

        # Add second command
        s.cmd("G1", x=25, y=36, e=0.05)
        self.assertEqual(len(s._commands), 2)

    def test_generate_gcode(self):
        """Test if generates correct gcode"""
        expected_output = "M73 P0 R0                          ; set print progress\n" \
                          "M205 X10 Y10 Z0.2 E4.5             ; sets the jerk limits, mm/sec\n" \
                          "M207                               ; Fans off\n"
        self.assertEqual(expected_output, self.s.generate())

    def test_custom_indent(self):
        """Test if sequence applies a custom comment indentation"""
        expected_output = "M73 P0 R0                ; set print progress\n" \
                          "M205 X10 Y10 Z0.2 E4.5   ; sets the jerk limits, mm/sec\n" \
                          "M207                     ; Fans off\n"
        self.assertEqual(expected_output, self.s.generate(comment_indent=25))

    def test_no_comment(self):
        """Test if sequence applies a custom comment indentation"""
        expected_output = "M73 P0 R0\n" \
                          "M205 X10 Y10 Z0.2 E4.5\n" \
                          "M207\n"
        self.assertEqual(expected_output, self.s.generate(include_comments=False))

    def test_sub_sequence(self):
        """Test addition of a subsequence to a sequence"""
        main_sequence = Sequence()

        # Creates a subsequence that draws a square on the x,y plane
        sub_sequence = Sequence()
        sub_sequence.cmd("G1", x=10, y=0, e=0.2)
        sub_sequence.cmd("G1", x=10, y=10, e=0.2)
        sub_sequence.cmd("G1", x=0, y=10, e=0.2)
        sub_sequence.cmd("G1", x=0, y=0, e=0.2)

        # Adds the subsequence twice moving the z up between moves
        main_sequence.cmd("G28", comment="Home axes")
        main_sequence.cmd("G1", z=0.2)
        main_sequence.sub(sub_sequence)
        main_sequence.cmd("G1", z=0.4)
        main_sequence.sub(sub_sequence)

        expected_output = "G28                                ; Home axes\n" \
                          "G1 Z0.2\n" \
                          "G1 X10 Y0 E0.2\n" \
                          "G1 X10 Y10 E0.2\n" \
                          "G1 X0 Y10 E0.2\n" \
                          "G1 X0 Y0 E0.2\n" \
                          "G1 Z0.4\n" \
                          "G1 X10 Y0 E0.2\n" \
                          "G1 X10 Y10 E0.2\n" \
                          "G1 X0 Y10 E0.2\n" \
                          "G1 X0 Y0 E0.2\n" \

        self.assertEqual(expected_output, main_sequence.generate())

    def test_variables(self):
        """Test adding variables to a sequence"""
        self.fail()
