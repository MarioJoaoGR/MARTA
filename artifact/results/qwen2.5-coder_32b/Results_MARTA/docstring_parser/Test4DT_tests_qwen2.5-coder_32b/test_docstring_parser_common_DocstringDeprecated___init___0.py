
import pytest
from typing import List, Optional
from docstring_parser.common import DocstringDeprecated





def test_valid_instantiation_full():
    deprecation_info = DocstringDeprecated(
        args=['old_arg1', 'old_arg2'],
        description='Use new_arg1 and new_arg2 instead.',
        version='1.2.0'
    )
    assert deprecation_info.description == 'Use new_arg1 and new_arg2 instead.'
    assert deprecation_info.version == '1.2.0'