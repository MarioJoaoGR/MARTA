
import re
from dataclasses_json.stringcase import spinalcase

def test_empty_string():
    assert spinalcase("") == ''
