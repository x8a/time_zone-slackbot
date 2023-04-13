import unittest
import commands

class TestTimezonebot(unittest.TestCase):

    def test_split(self):
        input = 'now paris munich'
        expected_output = ['now', 'paris']
        output = commands.parse_command(input)
        self.assertEqual(output, expected_output)
        self.assertEqual(len(output), 2)

if __name__ == '__main__':
    unittest.main()
