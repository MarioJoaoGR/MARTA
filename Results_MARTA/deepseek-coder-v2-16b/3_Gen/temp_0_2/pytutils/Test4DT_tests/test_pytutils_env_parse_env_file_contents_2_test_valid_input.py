
import re
import typing
from pytutils.env import parse_env_file_contents

def test_valid_input():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    expected_output = [('TEST', '${HOME}/yeee'), ('THISIS', '~/a/test'), ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]
    
    parsed_lines = list(parse_env_file_contents(lines))
    
    assert parsed_lines == expected_output
