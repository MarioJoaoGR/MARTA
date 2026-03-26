
import pytest
from io import StringIO
from isort.format import BasicPrinter

def test_diff_line():
    output = StringIO()
    printer = BasicPrinter(success='Success!', error='Error occurred.', output=output)
    
    # Test writing a line to the output
    line = "Hello, world!"
    printer.diff_line(line)
    assert output.getvalue().strip() == line
