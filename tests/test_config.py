import pytest
from scow.config import Config


config = Config()


def test_initial_chainmap_config_blank():
    assert len(config.data) == 0


def test_initial_persistent_blank():
    assert len(config.persistent) == 0


def test_initial_override_blank():
    assert len(config.override) == 0
