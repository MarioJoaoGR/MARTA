
import re
import pytest
from pytutils.env import parse_env_file_contents

def test_invalid_format():
    lines = ['INVALIDFORMAT', 'ANOTHERONE=value']
    parser = list(parse_env_file_contents(lines))
    assert len(parser) == 1
    assert parser[0] == ('ANOTHERONE', 'value')
