import pytest
from scow.config import Config


class TestConfigBlank(object):
    config = Config()

    def test_initial_chainmap_config_blank(self):
        assert len(self.config.data) == 0

    def test_initial_persistent_blank(self):
        assert len(self.config.persistent) == 0

    def test_initial_override_blank(self):
        assert len(self.config.override) == 0

    def test_merge(self):
        assert self.config._merge(
            {'test1': 'test'},
            {'test2': 'test'}
        ) == {'test1': 'test', 'test2': 'test'}

    def test_chain(self):
        assert self.config._chain(
            {'test1': 'test'},
            {'test2': 'test'}
        ) == {'test1': 'test', 'test2': 'test'}
