
import pytest
from dataclasses_json.stringcase import spinalcase  # Assuming this is the correct module and function name

def test_edge_case_empty_string():
    assert spinalcase("") == ''
