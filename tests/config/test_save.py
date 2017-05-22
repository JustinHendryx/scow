import pytest
import os
from scow.config import Config

tests_dir = os.path.dirname(os.path.abspath(__file__))


class TestConfigSave(object):
    config = Config(tests_dir + '/json/config_save.json')

    def test_load_from_json_config(self):
        self.config.load()

    def test_persistent_empty_from_empty_json(self):
        assert len(self.config.persistent) == 0

    def test_override_empty_from_empty_json(self):
        assert len(self.config.override) == 0

    def test_set_and_save_persistent_data_to_json(self):
        self.config.persistent['address'] = '10.0.0.1'
        self.config.persistent['port'] = 4321
        self.config.save()
