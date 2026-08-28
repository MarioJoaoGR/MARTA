
import pytest
from tornado.options import OptionParser
from tornado.log import enable_pretty_logging

def define_logging_options(options=None):
    """Add logging-related flags to an `OptionParser` instance or the default Tornado `options`.

    This function is designed to facilitate the configuration of command line options related to logging within a Tornado application. It enables users to set the Python log level, specify whether logs should be directed to stderr, define log file paths and sizes, and configure mechanisms for log rotation based on time intervals or file size.

    Parameters:
        options (Any, optional): The `OptionParser` instance to which the logging-related flags will be added. If not provided, it defaults to the global Tornado `options` instance.

    Examples:
        To add logging options to a custom `OptionParser` instance:
        
        ```python
        from tornado.options import OptionParser
        parser = OptionParser()
        define_logging_options(parser)
        ```

        If you are using the default Tornado `options` instance, simply call the function without arguments:
        
        ```python
        define_logging_options()
        ```

    Notes:
        - The function automatically adds several options to the provided `OptionParser` instance: "logging", "log_to_stderr", "log_file_prefix", and "log_file_max_size". Additional options for log rotation are also defined, including "log_file_num_backups", "log_rotate_when", and "log_rotate_interval".
        - The `logging` option allows you to set the Python log level. Accepted values include "debug", "info", "warning", "error", or "none". If set to "none", Tornado will not modify the existing logging configuration.
        - The `log_to_stderr` option determines whether log output should be sent to stderr, with colorization if possible. By default, this is set based on whether a log file prefix is specified and no other logging configurations are present.
        - The `log_file_prefix` option specifies the path prefix for log files. If running multiple Tornado processes, ensure that each process uses a different log file prefix to avoid conflicts.
        - The `log_file_max_size` option sets the maximum size of log files before they are rolled over.
        - Additional options such as "log_file_num_backups", "log_rotate_when", and "log_rotate_interval" control how logs are rotated based on either time intervals or file size.
    """
    if options is None:
        from tornado.options import options
        options = options
    
    options.define("logging", default="info", help="Set the Python log level.", metavar="debug|info|warning|error|none")
    options.define(
        "log_to_stderr",
        type=bool,
        default=None,
        help=(
            "Send log output to stderr (colorized if possible). "
            "By default use stderr if --log_file_prefix is not set and "
            "no other logging is configured."
        ),
    )
    options.define(
        "log_file_prefix",
        type=str,
        default=None,
        metavar="PATH",
        help=(
            "Path prefix for log files. "
            "Note that if you are running multiple Tornado processes, "
            "log_file_prefix must be different for each of them (e.g. "
            "include the port number)"
        ),
    )
    options.define(
        "log_file_max_size",
        type=int,
        default=100 * 1000 * 1000,
        help="max size of log files before rollover",
    )
    options.define("log_file_num_backups", type=int, default=10, help="number of log files to keep")
    options.define(
        "log_rotate_when",
        type=str,
        default="midnight",
        help=(
            "specify the type of TimedRotatingFileHandler interval "
            "other options:('S', 'M', 'H', 'D', 'W0'-'W6')"
        ),
    )
    options.define(
        "log_rotate_interval",
        type=int,
        default=1,
        help="The interval value of timed rotating",
    )
    options.define(
        "log_rotate_mode",
        type=str,
        default="size",
        help="The mode of rotating files(time or size)",
    )

    options.add_parse_callback(lambda: enable_pretty_logging())

def test_define_logging_options_default():
    parser = OptionParser()
    define_logging_options(parser)
    assert hasattr(parser, "logging")
    assert hasattr(parser, "log_to_stderr")
    assert hasattr(parser, "log_file_prefix")
    assert hasattr(parser, "log_file_max_size")
    assert hasattr(parser, "log_file_num_backups")
    assert hasattr(parser, "log_rotate_when")
    assert hasattr(parser, "log_rotate_interval")
    assert hasattr(parser, "log_rotate_mode")
