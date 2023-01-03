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
        self.assertIsInstance(added_command, Command)
        self.assertEqual(added_command, c)
