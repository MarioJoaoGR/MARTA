
import sys
import io
from pytutils.pretty import pp
import pytest

@pytest.mark.skip(reason="This is just an example of how you might write a test for the pp function.")
def test_valid_input():
    # Capture stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output

    # Define input data
    test_dict = {'key': 'value'}

    # Call the function with the test data
    pp(test_dict)

    # Get the output from the captured stdout
    output = captured_output.getvalue().strip()

    # Assert that the output is not empty (since pformat will always produce some output)
    assert output != ""

    # Reset stdout to its original value
    sys.stdout = sys.__stdout__
