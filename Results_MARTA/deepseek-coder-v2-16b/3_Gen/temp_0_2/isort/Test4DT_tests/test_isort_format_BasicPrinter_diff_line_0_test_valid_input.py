
import sys
from io import StringIO
from isort.format import BasicPrinter  # Correctly importing from 'isort.format'

def test_valid_input():
    output = StringIO()
    printer = BasicPrinter(success='Success!', error='Error occurred.', output=output)
    
    line_to_write = "Hello, world!"
    printer.diff_line(line_to_write)
    
    assert output.getvalue().strip() == line_to_write
