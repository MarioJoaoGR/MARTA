
import pytest
from ansible.executor.discovery.python_target import main
import json
from unittest.mock import patch

# Test case for the main function to ensure it calls get_platform_info and prints its result as JSON
def test_main():
    # Mocking the get_platform_info function to return a sample dictionary
    def mock_get_platform_info():
        return {
            'platform_dist_result': ['Ubuntu', ('18', '', '04')],
            'osrelease_content': 'NAME="Ubuntu"\nVERSION="18.04.3 LTS, Bionic Beaver"\nID=ubuntu\n...'
        }
    
    # Patching the get_platform_info function in the main module to use the mock implementation
    with patch('ansible.executor.discovery.python_target.get_platform_info', side_effect=mock_get_platform_info):
        # Redirecting stdout to capture the printed output
        from io import StringIO
        captured_output = StringIO()
        import sys
        old_stdout = sys.stdout
        sys.stdout = captured_output
        
        main()
        
        sys.stdout = old_stdout
        
        # Parsing the captured output to check if it matches the expected JSON format
        captured_output_str = captured_output.getvalue().strip()
        parsed_json = json.loads(captured_output_str)
        
        assert isinstance(parsed_json, dict), "The output should be a dictionary in JSON format"
        assert 'platform_dist_result' in parsed_json, "The expected key 'platform_dist_result' is missing"
        assert 'osrelease_content' in parsed_json, "The expected key 'osrelease_content' is missing"
        
        # Additional assertions to check the content of the keys if necessary

# Test case for handling an exception in get_platform_info
def test_main_exception():
    # Mocking the get_platform_info function to raise an exception
    def mock_get_platform_info(*args, **kwargs):
        raise Exception("Mocked error")
    
    with patch('ansible.executor.discovery.python_target.get_platform_info', side_effect=mock_get_platform_info):
        from io import StringIO
        captured_output = StringIO()
        import sys
        old_stdout = sys.stdout
        sys.stdout = captured_output
        
        with pytest.raises(Exception) as exc_info:
            main()
        
        assert str(exc_info.value) == "Mocked error", "The function should handle exceptions gracefully"
        
        sys.stdout = old_stdout
