
import subprocess
from pathlib import Path
from flutes.fs import get_file_lines

def test_valid_input():
    # Create a temporary file for testing
    temp_file = Path("temp_test_file.txt")
    with open(temp_file, 'w') as f:
        f.write("line1\nline2\nline3\n")
    
    try:
        # Test the function with a valid file path
        result = get_file_lines(temp_file)
        assert result == 3
        
        # Clean up the temporary file
        temp_file.unlink()
    except FileNotFoundError as e:
        print(f"File not found error: {e}")
        assert False, "Expected a valid file path but got an error."
    except subprocess.CalledProcessError as e:
        print(f"Subprocess error: {e}")
        assert False, "Expected no subprocess error but got one."
