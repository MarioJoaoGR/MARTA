
import pytest
from httpie.output.formatters.json import JSONFormatter

@pytest.fixture(scope="function")
def formatter():
    return JSONFormatter(format_options={'json': {'format': True, 'sort_keys': True, 'indent': 4}})

def test_valid_input_happy_path(formatter):
    body = '{"name": "Mario", "age": 30}'
    mime = 'application/json'
    
    formatted_body = formatter.format_body(body, mime)
    
    assert isinstance(formatted_body, str), "Expected a string output"
    assert json.loads(formatted_body) == {'age': 30, 'name': 'Mario'}, "Body should be properly formatted JSON"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_output_formatters_json_JSONFormatter_format_body_1_test_valid_input_happy_path
httpie/Test4DT_tests_codestral/test_httpie_output_formatters_json_JSONFormatter_format_body_1_test_valid_input_happy_path.py:16:11: E0602: Undefined variable 'json' (undefined-variable)


"""