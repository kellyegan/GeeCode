import unittest
from geecode import Command
from geecode import Sequence


class TestSequence(unittest.TestCase):

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
        s = Sequence()
        s.cmd("M73", p=0, r=0, comment="set print progress")
        s.cmd("M205", x=10, y=10, z=0.2, e=4.5, comment="sets the jerk limits, mm/sec")
        s.cmd("M207", comment="Fans off")
        expected_output = "M73 P0 R0                          ; set print progress\n" \
                          "M205 X10 Y10 Z0.2 E4.5             ; sets the jerk limits, mm/sec\n" \
                          "M207                               ; Fans off"
        self.assertEqual(expected_output, s.generate())