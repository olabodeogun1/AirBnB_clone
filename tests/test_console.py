import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand

class ConsoleTestCase(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        self.console = None

    def test_help_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help show")
            output = f.getvalue().strip()
            self.assertNotIn("Prints the string representation", output)

    def test_create_missing_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_create_invalid_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create InvalidClass")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")


if __name__ == '__main__':
    unittest.main()
