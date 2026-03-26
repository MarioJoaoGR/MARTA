# Module: isort.exceptions
# test_exceptions.py
from isort.exceptions import ExistingSyntaxErrors


def test_existing_syntax_errors_instantiation():
    try:
        raise ExistingSyntaxErrors("example_code.py")
    except ExistingSyntaxErrors as e:
        assert str(e) == "isort was told to sort imports within code that contains syntax errors: example_code.py."
        assert e.file_path == "example_code.py"

def test_existing_syntax_errors_try_except():
    try:
        # Simulate code that might cause syntax errors and require import sorting
        pass
    except ExistingSyntaxErrors as e:
        assert str(e) == "isort was told to sort imports within code that contains syntax errors: example_code.py."
        assert e.file_path == "example_code.py"
