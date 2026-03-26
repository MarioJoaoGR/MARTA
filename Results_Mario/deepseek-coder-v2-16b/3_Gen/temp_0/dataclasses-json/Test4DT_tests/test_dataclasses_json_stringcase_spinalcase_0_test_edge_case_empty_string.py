
import re
from dataclasses_json.stringcase import spinalcase as sc

def test_edge_case_empty_string():
    assert sc("") == ''
