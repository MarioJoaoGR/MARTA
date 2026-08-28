# Module: thonny.jedi_utils
import pytest
from thonny.jedi_utils import parse_source

# Test parsing a simple Python script
def test_parse_simple_script():
    python_script = """
    def hello_world():
        print('Hello, World!')
    """
    parsed_ast = parse_source(python_script)
    assert parsed_ast is not None, "Parsed AST should not be None"
    # Add more specific assertions if needed to validate the AST structure

# Test parsing a larger Python script with multiple functions and control structures
def test_parse_larger_script():
    python_script = """
    def main():
        print("Hello, Thonny!")
        for i in range(5):
            print(f"Iteration {i}")

    if __name__ == "__main__":
        main()
    """
    parsed_ast = parse_source(python_script)
    assert parsed_ast is not None, "Parsed AST should not be None"
    # Add more specific assertions to validate the structure of the larger script

# Test parsing a Python script with syntax errors
def test_parse_script_with_errors():
    python_script = """
    def main():
        print("Hello, Thonny!")
    if __name__ == "__main__":  # Syntax error: missing colon
        main()
    """
    parsed_ast = parse_source(python_script)
    assert parsed_ast is not None, "Parsed AST should not be None"
    # Add more specific assertions to validate how the parser handles syntax errors

# Additional test cases can be added here to cover different scenarios and edge cases
