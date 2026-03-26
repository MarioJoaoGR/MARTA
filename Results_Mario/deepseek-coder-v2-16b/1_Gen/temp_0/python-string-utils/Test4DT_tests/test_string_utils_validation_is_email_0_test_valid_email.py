
import re
from string_utils.validation import is_email

# Define the regex pattern for an email according to RFC 3696
EMAIL_RE = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

def test_valid_email():
    # Test a valid email address
    assert is_email('my.email@the-provider.com') == True
    
    # Test an invalid email due to too long a head part
    assert is_email('a' * 65 + '@gmail.com') == False
    
    # Test an invalid email due to multiple "@" signs
    assert is_email('@gmail.com') == False
    
    # Test a valid email with escaped spaces in the head part
    assert is_email('"my email"@example.com') == True
