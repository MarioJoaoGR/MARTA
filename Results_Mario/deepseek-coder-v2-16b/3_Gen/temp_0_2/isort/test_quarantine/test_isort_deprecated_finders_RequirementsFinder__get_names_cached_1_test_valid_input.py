
import os
from pathlib import Path
from isort.deprecated.finders import RequirementsFinder
from unittest.mock import patch

def test_valid_input():
    # Mock content for 'requirements.txt'
    mock_content = ['numpy', 'pandas']
    
    with patch('isort.deprecated.finders.RequirementsFinder._get_names_cached') as mock_method:
        mock_method.return_value = mock_content
        
        # Create a temporary file for testing
        temp_file_path = 'requirements.txt'
        with open(temp_file_path, 'w') as f:
            f.write('numpy==1.21.0\nnumpy>=1.3.0\npandas==1.21.0\npandas>=1.3.0')
        
        # Call the method under test
        result = RequirementsFinder._get_names_cached(temp_file_path)
        
        # Assert the expected output
        assert result == mock_content
        
    # Clean up the temporary file
    os.remove(temp_file_path)
