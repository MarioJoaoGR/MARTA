
import pytest
from io import StringIO
from isort.core import process
from isort.settings import DEFAULT_CONFIG

def test_edge_case():
    with open('empty_script.py', 'w') as f:
        pass  # Create an empty file named 'empty_script.py'
    
    input_stream = StringIO()  # Use a StringIO object for the input stream
    output_stream = StringIO()  # Use another StringIO object for the output stream
    
    with open('empty_script.py', 'r') as f:
        process(f, output_stream, config=DEFAULT_CONFIG)  # Process the empty file
    
    assert output_stream.getvalue().strip() == ""  # Check that the output is empty
