
import re
from string_utils.manipulation import slugify

def test_valid_input():
    # Test case 1: Standard title conversion
    assert slugify('Top 10 Reasons To Love Dogs!!!') == 'top-10-reasons-to-love-dogs'
    
    # Test case 2: Handling non-ASCII characters
    assert slugify('Mönstér Mägnët') == 'monster-magnet'
