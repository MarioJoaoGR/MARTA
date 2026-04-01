
import pytest
import logging
from pytutils.log import configure, DEFAULT_CONFIG, get_config

@pytest.mark.parametrize("config", [
    {'version': 1, 'handlers': [{'type': 'console'}], 'disable_existing_loggers': False},
    {'version': 1, 'handlers': [{'type': 'file', 'filename': 'app.log'}]},
])
def test_valid_config(config):
    configure(config=config)
    log = logging.getLogger(__name__)
    assert len(logging.root.handlers) == 1, "Expected one handler to be configured"
    if 'console' in config['handlers'][0]['type']:
        console_handler = logging.StreamHandler()
        assert isinstance(log.handlers[0], type(console_handler)), "Expected a console handler"
    elif 'file' in config['handlers'][0]['type']:
        file_handler = logging.FileHandler('app.log')
        assert isinstance(log.handlers[0], type(file_handler)), "Expected a file handler"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

pytutils/Test4DT_tests/test_pytutils_log_configure_0_test_valid_config.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
__________________________ test_valid_config[config0] __________________________

self = <logging.config.DictConfigurator object at 0x7f37bbec6110>

    def configure(self):
        """Do the configuration."""
    
        config = self.config
        if 'version' not in config:
            raise ValueError("dictionary doesn't specify a version")
        if config['version'] != 1:
            raise ValueError("Unsupported version: %s" % config['version'])
        incremental = config.pop('incremental', False)
        EMPTY_DICT = {}
        logging._acquireLock()
        try:
            if incremental:
                handlers = config.get('handlers', EMPTY_DICT)
                for name in handlers:
                    if name not in logging._handlers:
                        raise ValueError('No handler found with '
                                         'name %r'  % name)
                    else:
                        try:
                            handler = logging._handlers[name]
                            handler_config = handlers[name]
                            level = handler_config.get('level', None)
                            if level:
                                handler.setLevel(logging._checkLevel(level))
                        except Exception as e:
                            raise ValueError('Unable to configure handler '
                                             '%r' % name) from e
                loggers = config.get('loggers', EMPTY_DICT)
                for name in loggers:
                    try:
                        self.configure_logger(name, loggers[name], True)
                    except Exception as e:
                        raise ValueError('Unable to configure logger '
                                         '%r' % name) from e
                root = config.get('root', None)
                if root:
                    try:
                        self.configure_root(root, True)
                    except Exception as e:
                        raise ValueError('Unable to configure root '
                                         'logger') from e
            else:
                disable_existing = config.pop('disable_existing_loggers', True)
    
                _clearExistingHandlers()
    
                # Do formatters first - they don't refer to anything else
                formatters = config.get('formatters', EMPTY_DICT)
                for name in formatters:
                    try:
                        formatters[name] = self.configure_formatter(
                                                            formatters[name])
                    except Exception as e:
                        raise ValueError('Unable to configure '
                                         'formatter %r' % name) from e
                # Next, do filters - they don't refer to anything else, either
                filters = config.get('filters', EMPTY_DICT)
                for name in filters:
                    try:
                        filters[name] = self.configure_filter(filters[name])
                    except Exception as e:
                        raise ValueError('Unable to configure '
                                         'filter %r' % name) from e
    
                # Next, do handlers - they refer to formatters and filters
                # As handlers can refer to other handlers, sort the keys
                # to allow a deterministic order of configuration
                handlers = config.get('handlers', EMPTY_DICT)
                deferred = []
                for name in sorted(handlers):
                    try:
>                       handler = self.configure_handler(handlers[name])

/usr/local/lib/python3.11/logging/config.py:573: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = [{'type': 'console'}], key = {'type': 'console'}

    def __getitem__(self, key):
>       value = list.__getitem__(self, key)
E       TypeError: list indices must be integers or slices, not dict

/usr/local/lib/python3.11/logging/config.py:350: TypeError

The above exception was the direct cause of the following exception:

config = {'disable_existing_loggers': False, 'handlers': [{'type': 'console'}], 'version': 1}

    @pytest.mark.parametrize("config", [
        {'version': 1, 'handlers': [{'type': 'console'}], 'disable_existing_loggers': False},
        {'version': 1, 'handlers': [{'type': 'file', 'filename': 'app.log'}]},
    ])
    def test_valid_config(config):
>       configure(config=config)

pytutils/Test4DT_tests/test_pytutils_log_configure_0_test_valid_config.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pytutils/pytutils/log.py:96: in configure
    logging.config.dictConfig(cfg)
/usr/local/lib/python3.11/logging/config.py:823: in dictConfig
    dictConfigClass(config).configure()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <logging.config.DictConfigurator object at 0x7f37bbec6110>

    def configure(self):
        """Do the configuration."""
    
        config = self.config
        if 'version' not in config:
            raise ValueError("dictionary doesn't specify a version")
        if config['version'] != 1:
            raise ValueError("Unsupported version: %s" % config['version'])
        incremental = config.pop('incremental', False)
        EMPTY_DICT = {}
        logging._acquireLock()
        try:
            if incremental:
                handlers = config.get('handlers', EMPTY_DICT)
                for name in handlers:
                    if name not in logging._handlers:
                        raise ValueError('No handler found with '
                                         'name %r'  % name)
                    else:
                        try:
                            handler = logging._handlers[name]
                            handler_config = handlers[name]
                            level = handler_config.get('level', None)
                            if level:
                                handler.setLevel(logging._checkLevel(level))
                        except Exception as e:
                            raise ValueError('Unable to configure handler '
                                             '%r' % name) from e
                loggers = config.get('loggers', EMPTY_DICT)
                for name in loggers:
                    try:
                        self.configure_logger(name, loggers[name], True)
                    except Exception as e:
                        raise ValueError('Unable to configure logger '
                                         '%r' % name) from e
                root = config.get('root', None)
                if root:
                    try:
                        self.configure_root(root, True)
                    except Exception as e:
                        raise ValueError('Unable to configure root '
                                         'logger') from e
            else:
                disable_existing = config.pop('disable_existing_loggers', True)
    
                _clearExistingHandlers()
    
                # Do formatters first - they don't refer to anything else
                formatters = config.get('formatters', EMPTY_DICT)
                for name in formatters:
                    try:
                        formatters[name] = self.configure_formatter(
                                                            formatters[name])
                    except Exception as e:
                        raise ValueError('Unable to configure '
                                         'formatter %r' % name) from e
                # Next, do filters - they don't refer to anything else, either
                filters = config.get('filters', EMPTY_DICT)
                for name in filters:
                    try:
                        filters[name] = self.configure_filter(filters[name])
                    except Exception as e:
                        raise ValueError('Unable to configure '
                                         'filter %r' % name) from e
    
                # Next, do handlers - they refer to formatters and filters
                # As handlers can refer to other handlers, sort the keys
                # to allow a deterministic order of configuration
                handlers = config.get('handlers', EMPTY_DICT)
                deferred = []
                for name in sorted(handlers):
                    try:
                        handler = self.configure_handler(handlers[name])
                        handler.name = name
                        handlers[name] = handler
                    except Exception as e:
                        if 'target not configured yet' in str(e.__cause__):
                            deferred.append(name)
                        else:
>                           raise ValueError('Unable to configure handler '
                                             '%r' % name) from e
E                                            ValueError: Unable to configure handler {'type': 'console'}

/usr/local/lib/python3.11/logging/config.py:580: ValueError
__________________________ test_valid_config[config1] __________________________

self = <logging.config.DictConfigurator object at 0x7f37bb378210>

    def configure(self):
        """Do the configuration."""
    
        config = self.config
        if 'version' not in config:
            raise ValueError("dictionary doesn't specify a version")
        if config['version'] != 1:
            raise ValueError("Unsupported version: %s" % config['version'])
        incremental = config.pop('incremental', False)
        EMPTY_DICT = {}
        logging._acquireLock()
        try:
            if incremental:
                handlers = config.get('handlers', EMPTY_DICT)
                for name in handlers:
                    if name not in logging._handlers:
                        raise ValueError('No handler found with '
                                         'name %r'  % name)
                    else:
                        try:
                            handler = logging._handlers[name]
                            handler_config = handlers[name]
                            level = handler_config.get('level', None)
                            if level:
                                handler.setLevel(logging._checkLevel(level))
                        except Exception as e:
                            raise ValueError('Unable to configure handler '
                                             '%r' % name) from e
                loggers = config.get('loggers', EMPTY_DICT)
                for name in loggers:
                    try:
                        self.configure_logger(name, loggers[name], True)
                    except Exception as e:
                        raise ValueError('Unable to configure logger '
                                         '%r' % name) from e
                root = config.get('root', None)
                if root:
                    try:
                        self.configure_root(root, True)
                    except Exception as e:
                        raise ValueError('Unable to configure root '
                                         'logger') from e
            else:
                disable_existing = config.pop('disable_existing_loggers', True)
    
                _clearExistingHandlers()
    
                # Do formatters first - they don't refer to anything else
                formatters = config.get('formatters', EMPTY_DICT)
                for name in formatters:
                    try:
                        formatters[name] = self.configure_formatter(
                                                            formatters[name])
                    except Exception as e:
                        raise ValueError('Unable to configure '
                                         'formatter %r' % name) from e
                # Next, do filters - they don't refer to anything else, either
                filters = config.get('filters', EMPTY_DICT)
                for name in filters:
                    try:
                        filters[name] = self.configure_filter(filters[name])
                    except Exception as e:
                        raise ValueError('Unable to configure '
                                         'filter %r' % name) from e
    
                # Next, do handlers - they refer to formatters and filters
                # As handlers can refer to other handlers, sort the keys
                # to allow a deterministic order of configuration
                handlers = config.get('handlers', EMPTY_DICT)
                deferred = []
                for name in sorted(handlers):
                    try:
>                       handler = self.configure_handler(handlers[name])

/usr/local/lib/python3.11/logging/config.py:573: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = [{'type': 'file', 'filename': 'app.log'}]
key = {'filename': 'app.log', 'type': 'file'}

    def __getitem__(self, key):
>       value = list.__getitem__(self, key)
E       TypeError: list indices must be integers or slices, not dict

/usr/local/lib/python3.11/logging/config.py:350: TypeError

The above exception was the direct cause of the following exception:

config = {'handlers': [{'filename': 'app.log', 'type': 'file'}], 'version': 1}

    @pytest.mark.parametrize("config", [
        {'version': 1, 'handlers': [{'type': 'console'}], 'disable_existing_loggers': False},
        {'version': 1, 'handlers': [{'type': 'file', 'filename': 'app.log'}]},
    ])
    def test_valid_config(config):
>       configure(config=config)

pytutils/Test4DT_tests/test_pytutils_log_configure_0_test_valid_config.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pytutils/pytutils/log.py:96: in configure
    logging.config.dictConfig(cfg)
/usr/local/lib/python3.11/logging/config.py:823: in dictConfig
    dictConfigClass(config).configure()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <logging.config.DictConfigurator object at 0x7f37bb378210>

    def configure(self):
        """Do the configuration."""
    
        config = self.config
        if 'version' not in config:
            raise ValueError("dictionary doesn't specify a version")
        if config['version'] != 1:
            raise ValueError("Unsupported version: %s" % config['version'])
        incremental = config.pop('incremental', False)
        EMPTY_DICT = {}
        logging._acquireLock()
        try:
            if incremental:
                handlers = config.get('handlers', EMPTY_DICT)
                for name in handlers:
                    if name not in logging._handlers:
                        raise ValueError('No handler found with '
                                         'name %r'  % name)
                    else:
                        try:
                            handler = logging._handlers[name]
                            handler_config = handlers[name]
                            level = handler_config.get('level', None)
                            if level:
                                handler.setLevel(logging._checkLevel(level))
                        except Exception as e:
                            raise ValueError('Unable to configure handler '
                                             '%r' % name) from e
                loggers = config.get('loggers', EMPTY_DICT)
                for name in loggers:
                    try:
                        self.configure_logger(name, loggers[name], True)
                    except Exception as e:
                        raise ValueError('Unable to configure logger '
                                         '%r' % name) from e
                root = config.get('root', None)
                if root:
                    try:
                        self.configure_root(root, True)
                    except Exception as e:
                        raise ValueError('Unable to configure root '
                                         'logger') from e
            else:
                disable_existing = config.pop('disable_existing_loggers', True)
    
                _clearExistingHandlers()
    
                # Do formatters first - they don't refer to anything else
                formatters = config.get('formatters', EMPTY_DICT)
                for name in formatters:
                    try:
                        formatters[name] = self.configure_formatter(
                                                            formatters[name])
                    except Exception as e:
                        raise ValueError('Unable to configure '
                                         'formatter %r' % name) from e
                # Next, do filters - they don't refer to anything else, either
                filters = config.get('filters', EMPTY_DICT)
                for name in filters:
                    try:
                        filters[name] = self.configure_filter(filters[name])
                    except Exception as e:
                        raise ValueError('Unable to configure '
                                         'filter %r' % name) from e
    
                # Next, do handlers - they refer to formatters and filters
                # As handlers can refer to other handlers, sort the keys
                # to allow a deterministic order of configuration
                handlers = config.get('handlers', EMPTY_DICT)
                deferred = []
                for name in sorted(handlers):
                    try:
                        handler = self.configure_handler(handlers[name])
                        handler.name = name
                        handlers[name] = handler
                    except Exception as e:
                        if 'target not configured yet' in str(e.__cause__):
                            deferred.append(name)
                        else:
>                           raise ValueError('Unable to configure handler '
                                             '%r' % name) from e
E                                            ValueError: Unable to configure handler {'type': 'file', 'filename': 'app.log'}

/usr/local/lib/python3.11/logging/config.py:580: ValueError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_log_configure_0_test_valid_config.py::test_valid_config[config0]
FAILED pytutils/Test4DT_tests/test_pytutils_log_configure_0_test_valid_config.py::test_valid_config[config1]
============================== 2 failed in 0.12s ===============================
"""