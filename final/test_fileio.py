import unittest
import os
from fileio import FileIO

a = open


class TestFileIO(unittest.TestCase):

    def test_write_file(self):
        test_file = 'test.txt'
        content = b'Hello, file!'

        FileIO.write_file(content, test_file)
        self.assertTrue(os.path.exists(test_file))

        read_content = a(test_file).read()
        self.assertEqual(content, read_content.encode())

        os.remove(test_file)

    def test_read_file(self):
        test_file = 'test.txt'
        content = b'Hello, file!'

        a(test_file, "w").write(content.decode())

        read_content = FileIO.read_file(test_file)
        self.assertEqual(content, read_content)

        os.remove(test_file)


if __name__ == '__main__':
    unittest.main()
