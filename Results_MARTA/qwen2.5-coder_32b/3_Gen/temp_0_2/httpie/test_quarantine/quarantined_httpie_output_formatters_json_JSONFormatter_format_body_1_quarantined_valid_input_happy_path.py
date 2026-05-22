
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
    try:
        json.loads(formatted_body)
    except ValueError:
        pytest.fail("Formatted body is not valid JSON")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_output_formatters_json_JSONFormatter_format_body_1_test_valid_input_happy_path
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_formatters_json_JSONFormatter_format_body_1_test_valid_input_happy_path.py:17:8: E0602: Undefined variable 'json' (undefined-variable)


"""