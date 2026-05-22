
import pytest
from httpie.output.formatters.json import JSONFormatter

@pytest.fixture(scope="function")
def setup_formatter():
    formatter = JSONFormatter(format_options={'json': {'format': True}})
    return formatter

def test_valid_input_happy_path(setup_formatter):
    body = '{"key": "value"}'
    mime = 'application/json'
    
    formatted_body = setup_formatter.format_body(body, mime)
    
    assert isinstance(formatted_body, str), "Expected a string output"
    try:
        json.loads(formatted_body)
    except ValueError:
        pytest.fail("Formatted body is not valid JSON")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_output_formatters_json_JSONFormatter_format_body_0_test_valid_input_happy_path
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_json_JSONFormatter_format_body_0_test_valid_input_happy_path.py:18:8: E0602: Undefined variable 'json' (undefined-variable)


"""