
from pathlib import Path
from isort.place import Config, module_with_reason, DEFAULT_CONFIG

def test_valid_input_happy_path():
    config = Config(forced_separate=['*.log', 'data.*'], known_patterns=[("^abc.*", "section1"), ("^def.*", "section2")], src_paths=[Path("C:\\PythonProjects\\myproject")])
    
    # The expected result should be the string representation of the wildcard pattern, not just '*'
    assert module_with_reason("example.log", config)[0] == '*.log'
