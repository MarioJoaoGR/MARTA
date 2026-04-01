
import pytest
from io import StringIO
from isort.core import process
from isort.settings import DEFAULT_CONFIG

def test_valid_input():
    # Arrange
    input_content = """
    def func1():
        pass
    from moduleB import variableC
    import moduleD
    print("Hello, World!")
    """
    expected_output = """
    def func1():
        pass
    import moduleD
    from moduleB import variableC
    print("Hello, World!")
    """
    
    input_stream = StringIO(input_content)
    output_stream = StringIO()
    
    # Act
    result = process(input_stream, output_stream, config=DEFAULT_CONFIG)
    
    # Assert
    input_stream.seek(0)
    output_stream.seek(0)
    assert input_stream.read() != output_stream.read(), "The content should be sorted."
    assert result is True, "The function should return True indicating changes were made."
