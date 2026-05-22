
import re
from httpie.output.processing import is_valid_mime  # Assuming the function and module are imported correctly from httpie.output.processing

# Define a mock MIME regular expression pattern for testing purposes
MIME_RE = re.compile(r'^[a-zA-Z]+\/[a-zA-Z]+$')

def test_is_valid_mime_basic():
    # Test cases with known valid and invalid MIME types
    assert is_valid_mime("image/png")  # Expected to be True
    assert is_valid_mime("text/html")  # Expected to be True
    assert is_valid_mime("application/pdf")  # Expected to be True
    assert not is_valid_mime("invalid-mime")  # Expected to be False
