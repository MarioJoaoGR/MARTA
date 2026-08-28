
import pytest
from ansible.config.manager import ConfigManager

@pytest.fixture(scope="module")
def config_manager():
    return ConfigManager()



def test_parsing_specific_configuration_file(tmp_path):
    conf_file = tmp_path / "custom_settings.ini"
    conf_file.write_text("[section]\nkey=value")
    
    config = ConfigManager()
    config._parse_config_file(str(conf_file))
    assert config._parsers[str(conf_file)].get("section", "key") == "value"

    # Add more assertions to verify the behavior with default definitions file