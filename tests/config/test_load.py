import pytest
import os
from scow.config import Config

tests_dir = os.path.dirname(os.path.abspath(__file__))


class TestConfigLoad(object):
    config = Config(tests_dir + '/json/config.json')

    def test_load_from_json_config(self):
        self.config.load()

    def test_loaded_data_from_persistent(self):
        assert self.config.persistent['address'] == '127.0.0.1'
        assert self.config.persistent['port'] == 1234

    def test_loaded_data_from_chainmap(self):
        assert self.config.data['address'] == '127.0.0.1'
        assert self.config.data['port'] == 1234

    def test_override_empty_after_config_loaded(self):
        assert len(self.config.override) == 0
