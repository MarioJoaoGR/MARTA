
import pytest
from flutes.network import _extract_google_drive_file_id

# Test cases for _extract_google_drive_file_id function

def test_extract_google_drive_file_id_standard():
    url = 'https://drive.google.com/file/d/1aBcD2eF3gHiJkLmNoPqRsTuVwXyZa/view?usp=sharing'
    expected_output = '1aBcD2eF3gHiJkLmNoPqRsTuVwXyZa'
    assert _extract_google_drive_file_id(url) == expected_output

def test_extract_google_drive_file_id_alternative():
    url = 'https://drive.google.com/open?id=1aBcD2eF3gHiJkLmNoPqRsTuVwXyZa'
    expected_output = '1aBcD2eF3gHiJkLmNoPqRsTuVwXyZa'