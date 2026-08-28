
import pytest
from unittest.mock import patch, MagicMock
from lib.ansible.plugins.lookup import LookupModule
import csv
import io

# Test data for valid input scenario
VALID_CSV_DATA = """key1,value1
key2,value2
"""

# Test data for missing key scenario
MISSING_KEY_CSV_DATA = """key1,value1
key2,value2
"""

# Test data for invalid file scenario
INVALID_FILE_PATH = "nonexistentfile.csv"

class TestLookupModule:
    
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        self.lookup = LookupModule()

    # Scenario 1: test_valid_input
    def test_valid_input(self, tmpdir):
        filename = str(tmpdir / "test.csv")
        with open(filename, 'w') as f:
            f.write(VALID_CSV_DATA)
        
        result = self.lookup.read_csv(filename, 'key1', ',')
        assert result == 'value1'

    # Scenario 2: test_missing_key
    def test_missing_key(self, tmpdir):
        filename = str(tmpdir / "test.csv")
        with open(filename, 'w') as f:
            f.write(MISSING_KEY_CSV_DATA)
        
        result = self.lookup.read_csv(filename, 'missing_key', ',')
        assert result is None

    # Scenario 3: test_invalid_file
    def test_invalid_file(self):
        with pytest.raises(Exception):
            self.lookup.read_csv(INVALID_FILE_PATH, 'key1', ',')
