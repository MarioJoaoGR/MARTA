
import re
from unittest.mock import patch
from ansible.module_utils.common.dict_transformations import _camel_to_snake


def test_basic_conversion():
    with patch('ansible.module_utils.common.dict_transformations._camel_to_snake', return_value='camel_case_name'):
        assert _camel_to_snake("CamelCaseName") == 'camel_case_name'

def test_conversion_with_reversible():
    with patch('ansible.module_utils.common.dict_transformations._camel_to_snake', return_value='another_camel_case_example'):
        assert _camel_to_snake("AnotherCamelCaseExample", reversible=True) == 'another_camel_case_example'