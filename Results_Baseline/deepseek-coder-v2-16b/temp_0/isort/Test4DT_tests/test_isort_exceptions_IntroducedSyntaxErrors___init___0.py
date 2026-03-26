# Module: isort.exceptions
# Import the function from its module
from isort.exceptions import IntroducedSyntaxErrors


def test_introduced_syntax_errors_initialization():
    # Test case 1: Initialize with a valid file path
    try:
        raise IntroducedSyntaxErrors("path/to/your_file.py")
    except IntroducedSyntaxErrors as e:
        assert str(e) == "isort introduced syntax errors when attempting to sort the imports contained within path/to/your_file.py."
        assert e.file_path == "path/to/your_file.py"

    # Test case 2: Initialize with a different valid file path
    try:
        raise IntroducedSyntaxErrors("path/to/another_file.py")
    except IntroducedSyntaxErrors as e:
        assert str(e) == "isort introduced syntax errors when attempting to sort the imports contained within path/to/another_file.py."
        assert e.file_path == "path/to/another_file.py"

    # Test case 3: Initialize with an invalid file path (should raise a TypeError)
    try:
        IntroducedSyntaxErrors(12345)  # Passing an integer instead of a string
    except TypeError as e:
        assert str(e) == "IntroducedSyntaxErrors.__init__() missing 1 required positional argument: 'file_path'"
