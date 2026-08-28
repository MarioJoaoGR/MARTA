
import pytest
from unittest.mock import patch
from youtube_dl.jsinterp import JSInterpreter, ExtractorError



def test_invalid_function_extraction():
    interpreter = JSInterpreter("function add(a, b) { return a + b; }")
    with patch('youtube_dl.jsinterp.re') as mock_re:
        mock_re.search.return_value = None
        with pytest.raises(ExtractorError):
            interpreter.extract_function('subtract')