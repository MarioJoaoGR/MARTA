
import pytest
from dataclasses_json.stringcase import pascalcase

def test_edge_case_empty_string():
    assert pascalcase("") == ''
