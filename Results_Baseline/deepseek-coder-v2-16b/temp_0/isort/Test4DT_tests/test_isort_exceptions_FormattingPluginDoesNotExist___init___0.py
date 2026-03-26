# Module: isort.exceptions
# test_exceptions.py
from isort.exceptions import FormattingPluginDoesNotExist


def test_formattingplugindoesnotexist_exception():
    try:
        raise FormattingPluginDoesNotExist("json_formatter")
    except FormattingPluginDoesNotExist as e:
        assert str(e) == "Specified formatting plugin of json_formatter does not exist. "
        assert e.formatter == "json_formatter"
