
import unittest.mock
from httpie.cli.options import Group
import textwrap

class TestGroupFinalize(unittest.TestCase):
    def test_valid_input(self):
        group = Group(name="example_group")
        group.description = "  This is an example group.\nWith multiple lines."
    
        # Mock the textwrap.dedent function to ensure it's not actually called during the test
        with unittest.mock.patch('textwrap.dedent', return_value='This is an example group.\nWith multiple lines.'):
            group.finalize()
            self.assertEqual(group.description, 'This is an example group.\nWith multiple lines.')
