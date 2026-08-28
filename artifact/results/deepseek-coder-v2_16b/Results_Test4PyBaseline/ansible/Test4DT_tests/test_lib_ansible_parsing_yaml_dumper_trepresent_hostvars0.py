# Module: ansible.parsing.yaml.dumper
# Import the function using its provided module name
from ansible.parsing.yaml.dumper import represent_hostvars
import pytest

# Test case for representing host variables in a structured format suitable for YAML representation
def test_represent_hostvars():
    # Create an instance of self (assuming it has the necessary method)
    class Self:
        def represent_dict(self, data):
            return {key: value for key, value in data.items()}
    
    # Define the input data
    data = {
        'host1': {'var1': 1, 'var2': 2},
        'host2': {'var3': 3, 'var4': 4}
    }
    
    # Call the function with the instance and data
    result = represent_hostvars(Self(), data)
    
    # Define the expected output
    expected_output = {
        'host1': {'var1': 1, 'var2': 2},
        'host2': {'var3': 3, 'var4': 4}
    }
    
    # Assert that the result matches the expected output
    assert result == expected_output

# Run the test case
if __name__ == "__main__":
    pytest.main()
