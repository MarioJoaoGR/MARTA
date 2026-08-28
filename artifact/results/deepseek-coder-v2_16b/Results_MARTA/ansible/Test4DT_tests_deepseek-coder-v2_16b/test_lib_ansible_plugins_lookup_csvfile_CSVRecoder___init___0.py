
import pytest
from ansible.plugins.lookup.csvfile import CSVRecoder
import codecs

def test_valid_init():
    # Arrange
    fake_file = open('test_data.csv', 'rb')  # Valid file object
    
    # Act
    recoder = CSVRecoder(fake_file, 'utf-8')
    
    # Assert
    assert isinstance(recoder, CSVRecoder), "Expected a CSVRecoder instance"
    assert fake_file.closed is False, "File should not be closed after initialization"
