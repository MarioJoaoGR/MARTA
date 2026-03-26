
import unittest
from docstring_parser import parse
import typing as T

class TestDeprecation(unittest.TestCase):
    def test_deprecation(self):
        source = """
            A short description.
            
            .. deprecated:: 1.0
                This function will be removed in version 1.0 of the library.
        """
        docstring = parse(source)
        self.assertIsNotNone(docstring.deprecation)
        self.assertEqual(docstring.deprecation.version, "1.0")
        self.assertEqual(docstring.deprecation.description, "This function will be removed in version 1.0 of the library.")

    def test_deprecation_no_version(self):
        source = """
            A short description.
            
            .. deprecated::
                This function will be removed without specifying a version.
        """
        docstring = parse(source)
        self.assertIsNotNone(docstring.deprecation)
        self.assertIsNone(docstring.deprecation.version)
        self.assertEqual(docstring.deprecation.description, "This function will be removed without specifying a version.")

    def test_deprecation_no_description(self):
        source = """
            A short description.
            
            .. deprecated:: 1.0
        """
        docstring = parse(source)
        self.assertIsNotNone(docstring.deprecation)
        self.assertEqual(docstring.deprecation.version, "1.0")
        self.assertIsNone(docstring.deprecation.description)

    def test_deprecation_no_content(self):
        source = """
            A short description without any deprecation note.
        """
        docstring = parse(source)
        self.assertIsNone(docstring.deprecation)
