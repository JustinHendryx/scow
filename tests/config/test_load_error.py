import pytest
import os
from scow.config import Config

tests_dir = os.path.dirname(os.path.abspath(__file__))


class TestConfigLoadError(object):
    config = Config(tests_dir + '/json/config_nonexistent.json')

    def test_load_from_json_config(self):
        with pytest.raises(Exception):
            self.config.load()
