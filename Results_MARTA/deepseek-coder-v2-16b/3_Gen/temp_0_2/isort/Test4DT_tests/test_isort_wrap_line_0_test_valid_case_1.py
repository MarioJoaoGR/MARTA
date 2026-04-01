
import re
from isort.wrap import line, Config, DEFAULT_CONFIG, Modes

def test_valid_case_1():
    config = Config(line_length=80)
    content = "This is a short line of text that does not need to be wrapped."
    expected_output = "This is a short line of text that does not need to be wrapped."
    
    assert line(content, "\n", config) == expected_output
