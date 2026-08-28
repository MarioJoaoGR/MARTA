
import pytest
from tornado.options import OptionParser

# Import the function to be tested
from tornado.log import define_logging_options

def test_define_logging_options_default():
    parser = OptionParser()
    define_logging_options(parser)
    
    # Check if default options are added correctly
    assert parser.logging == "info"
    assert parser.log_to_stderr is None  # Default value should be None
    assert parser.log_file_prefix is None
    assert parser.log_file_max_size == 100 * 1000 * 1000
    assert parser.log_file_num_backups == 10
    assert parser.log_rotate_when == "midnight"
    assert parser.log_rotate_interval == 1
    assert parser.log_rotate_mode == "size"

def test_define_logging_options_custom():
    parser = OptionParser()
    define_logging_options(parser)
    
    # Modify some options and check if they are updated correctly
    parser.logging = "debug"
    parser.log_to_stderr = True
    parser.log_file_prefix = "/path/to/logfile"
    parser.log_file_max_size = 200 * 1000 * 1000
    parser.log_file_num_backups = 5
    parser.log_rotate_when = "H"
    parser.log_rotate_interval = 6
    parser.log_rotate_mode = "time"
    
    # Check if the custom options are correctly set
    assert parser.logging == "debug"
    assert parser.log_to_stderr is True
    assert parser.log_file_prefix == "/path/to/logfile"
    assert parser.log_file_max_size == 200 * 1000 * 1000
    assert parser.log_file_num_backups == 5
    assert parser.log_rotate_when == "H"
    assert parser.log_rotate_interval == 6
    assert parser.log_rotate_mode == "time"

def test_define_logging_options_none():
    # Create a custom OptionParser instance
    parser = OptionParser()
    
    # Call the function without any parameters to use the default options
    define_logging_options(parser)  # Passing None should not be used here
    
    # Check if default options are added correctly
    assert parser.logging == "info"
    assert parser.log_to_stderr is None  # Default value should be None
    assert parser.log_file_prefix is None
    assert parser.log_file_max_size == 100 * 1000 * 1000
    assert parser.log_file_num_backups == 10
    assert parser.log_rotate_when == "midnight"
    assert parser.log_rotate_interval == 1
    assert parser.log_rotate_mode == "size"
