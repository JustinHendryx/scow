import pytest
import os
from scow.config import Config

tests_dir = os.path.dirname(os.path.abspath(__file__))


class TestConfigOverride(object):
    config = Config(tests_dir + '/json/config.json', [{'address': '0.0.0.0'}])

    def test_load_from_json_config(self):
        self.config.load()

    def test_loaded_data_from_override(self):
        assert self.config.override['address'] == '0.0.0.0'
        assert len(self.config.override) == 1

    def test_loaded_data_from_persistent(self):
        assert self.config.persistent['port'] == 1234
        assert len(self.config.persistent) == 2

    def test_loaded_data_from_chainmap(self):
        assert self.config.data['address'] == '0.0.0.0'
        assert self.config.data['port'] == 1234
