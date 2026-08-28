# Module: isort.exceptions
# test_exceptions.py
from isort.exceptions import ExistingSyntaxErrors

def test_existing_syntax_errors():
    try:
        raise ExistingSyntaxErrors("example_file.py")
    except ExistingSyntaxErrors as e:
        assert str(e) == "isort was told to sort imports within code that contains syntax errors: example_file.py."

def test_existing_syntax_errors_with_different_file():
    try:
        raise ExistingSyntaxErrors("test_file.py")
    except ExistingSyntaxErrors as e:
        assert str(e) == "isort was told to sort imports within code that contains syntax errors: test_file.py."
