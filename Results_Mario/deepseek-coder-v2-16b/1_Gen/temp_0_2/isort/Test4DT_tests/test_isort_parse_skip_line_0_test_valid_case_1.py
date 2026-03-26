
import pytest
from isort.parse import skip_line  # Importing the function correctly

def test_valid_case_1():
    line = "print('Hello, World!')"
    in_quote = ''
    index = 0
    section_comments = ()
    needs_import = True
    
    result = skip_line(line, in_quote, index, section_comments, needs_import)
    
    assert not result[0], "Expected the line to be processed as it is not within a quoted section and does not contain import statements."
    assert result[1] == '', "Expected no change in quote state since the line is not within quotes."
