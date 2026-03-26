
import pytest
from flutes.network import _extract_google_drive_file_id

# Test cases for _extract_google_drive_file_id function

def test_valid_file_url():
    url = "https://drive.google.com/file/d/1aBcD2eF3gHiJkLmNoPqRsT/view?usp=sharing"
    assert _extract_google_drive_file_id(url) == '1aBcD2eF3gHiJkLmNoPqRsT'

def test_valid_folder_url():
    url = "https://drive.google.com/drive/folders/1aBcD2eF3gHiJkLmNoPqRsT"