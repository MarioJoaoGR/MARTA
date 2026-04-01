
from isort._vendored.tomli._parser import load
import warnings
from io import StringIO

def test_none_input():
    # Create a mock file object with no content
    fp = StringIO()
    
    # Call the function and check if it handles empty input correctly
    parsed_data = load(fp)
    assert parsed_data == {}
