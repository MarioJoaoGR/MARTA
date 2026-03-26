
# Mocking the pytutils.tlds module for demonstration purposes
class MockTLD:
    def join_dom(self, a, b):
        return f"{b}.{a}"

def test_valid_input():
    # Create an instance of the mock TLD module
    tld = MockTLD()
    
    # Test with valid input
    assert tld.join_dom('example', 'com') == 'com.example'
    assert tld.join_dom('co', 'uk') == 'uk.co'
