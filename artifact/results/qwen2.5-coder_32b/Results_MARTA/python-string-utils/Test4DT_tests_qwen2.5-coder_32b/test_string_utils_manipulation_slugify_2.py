
import pytest
from string_utils.manipulation import slugify, InvalidInputError

def test_happy_path():
    result = slugify('Top 10 Reasons To Love Dogs!!!')
    assert result == 'top-10-reasons-to-love-dogs'

def test_edge_cases():
    # Test with empty string
    result_empty = slugify('')
    assert result_empty == ''

    # Test with None (should raise InvalidInputError)
    with pytest.raises(InvalidInputError):
        slugify(None)

    # Test with only spaces
    result_spaces = slugify('   ')
    assert result_spaces == ''

    # Test with a string containing all special characters
    result_special_chars = slugify('A!B@C#D$E%F^G&H*I(J)K_L+M=N{O}P[Q]R\\S;T:"U\'<V>,W./X?Y`Z~')
    assert result_special_chars == 'a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z'

def test_invalid_inputs():
    # Test with integer input (should raise InvalidInputError)
    with pytest.raises(InvalidInputError):
        slugify(12345)

    # Test with list input (should raise InvalidInputError)
    with pytest.raises(InvalidInputError):
        slugify(['list', 'of', 'strings'])

    # Test with dictionary input (should raise InvalidInputError)
    with pytest.raises(InvalidInputError):
        slugify({'key': 'value'})
