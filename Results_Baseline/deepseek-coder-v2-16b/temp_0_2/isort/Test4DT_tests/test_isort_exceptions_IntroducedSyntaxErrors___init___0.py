# Module: isort.exceptions
# test_exceptions.py
from isort.exceptions import IntroducedSyntaxErrors


def test_introduced_syntax_errors():
    try:
        raise IntroducedSyntaxErrors("test/file/path.py")
    except IntroducedSyntaxErrors as e:
        assert str(e) == "isort introduced syntax errors when attempting to sort the imports contained within test/file/path.py."
        assert e.file_path == "test/file/path.py"

def test_introduced_syntax_errors_with_different_path():
    try:
        raise IntroducedSyntaxErrors("another/example/file.py")
    except IntroducedSyntaxErrors as e:
        assert str(e) == "isort introduced syntax errors when attempting to sort the imports contained within another/example/file.py."
        assert e.file_path == "another/example/file.py"
