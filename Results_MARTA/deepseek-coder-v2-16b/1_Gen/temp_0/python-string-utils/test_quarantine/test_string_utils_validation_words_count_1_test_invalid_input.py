
import re
from unittest.mock import patch
from string_utils.validation import InvalidInputError, is_string

# Assuming WORDS_COUNT_RE is defined somewhere in your code or module
WORDS_COUNT_RE = re.compile(r'\b\w+\b')

def words_count(input_string: str) -> int:
    """
    Returns the number of words contained into the given string.
    
    This method considers sequences of one or more letters and/or numbers as "words", ignoring punctuation and other non-alphanumeric characters. It is aware that a sequence of alphanumeric characters separated by punctuation can be considered a word.
    
    *Examples:*
    
    - For the string `'hello world'`, the function will return `2`.
    - For the string `'one,two,three.stop'`, the function will return `4`.
    
    :param input_string: The string to analyze for word count. This should be a sequence of letters and/or numbers with optional punctuation in between.
    :type input_string: str
    :return: The number of words identified in the input string based on the criteria described.
    """
    if not is_string(input_string):
        raise InvalidInputError(input_string)
    
    return len(WORDS_COUNT_RE.findall(input_string))

def test_invalid_input():
    # Test case 1: Non-string input should raise InvalidInputError
    with patch('string_utils.validation.is_string', return_value=False):
        with pytest.raises(InvalidInputError):
            words_count("test")
    
    # Test case 2: String with punctuation but no alphanumeric sequences should count as zero words
    assert words_count('! @ # % ... []') == 0
    
    # Test case 3: String with multiple words separated by punctuation should be counted correctly
    assert words_count('one,two,three.stop') == 4

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation_words_count_1_test_invalid_input
python-string-utils/Test4DT_tests/test_string_utils_validation_words_count_1_test_invalid_input.py:32:13: E0602: Undefined variable 'pytest' (undefined-variable)

"""