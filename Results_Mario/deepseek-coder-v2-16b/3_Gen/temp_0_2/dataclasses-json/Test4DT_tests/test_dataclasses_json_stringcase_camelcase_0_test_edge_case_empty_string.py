
import re
from dataclasses_json.stringcase import camelcase
import pytest

def test_edge_case_empty_string():
    assert camelcase("") == ''
