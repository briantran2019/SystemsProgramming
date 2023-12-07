import unittest
from command import Command


class TestCommand(unittest.TestCase):

    def test_run_command(self):
        result = Command.run_command(b'echo "Hello World"')
        self.assertIn("Hello World", result.decode())


if __name__ == '__main__':
    unittest.main()
