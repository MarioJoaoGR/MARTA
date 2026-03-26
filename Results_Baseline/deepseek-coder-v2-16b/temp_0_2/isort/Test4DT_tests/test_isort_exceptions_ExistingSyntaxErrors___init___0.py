# Module: isort.exceptions
# test_exceptions.py
from isort.exceptions import ExistingSyntaxErrors


def test_existing_syntax_errors_init():
    try:
        raise ExistingSyntaxErrors("test/path/to/your/file.py")
    except ExistingSyntaxErrors as e:
        assert str(e) == "isort was told to sort imports within code that contains syntax errors: test/path/to/your/file.py."
        assert e.file_path == "test/path/to/your/file.py"

def test_existing_syntax_errors_init_with_empty_string():
    try:
        raise ExistingSyntaxErrors("")
    except ExistingSyntaxErrors as e:
        assert str(e) == "isort was told to sort imports within code that contains syntax errors: ."
        assert e.file_path == ""
