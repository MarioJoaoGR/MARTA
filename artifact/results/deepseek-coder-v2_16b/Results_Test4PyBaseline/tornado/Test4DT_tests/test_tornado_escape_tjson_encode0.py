
import pytest
import json
from tornado.escape import json_encode

# Test cases for json_encode function
def test_json_encode_dict():
    value = {"key": "value", "script": "</script>"}
    encoded_json = json_encode(value)
    assert encoded_json == '{"key": "value", "script": "<\\/script>"}'

def test_json_encode_list():
    value = ["item1", "item2", {"nested": "object"}]
    encoded_json = json_encode(value)