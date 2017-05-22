import pytest
import os
from scow.config import Config

config_file = (os.path.dirname(os.path.abspath(__file__)) +
               '/configs/config.json')

config = Config()


def test_initial_chainmap_config_blank():
    assert len(config.data) == 0


def test_initial_persistent_blank():
    assert len(config.persistent) == 0


def test_initial_override_blank():
    assert len(config.override) == 0


def test_merge():
    assert config._merge(
        {'test1': 'test'},
        {'test2': 'test'}
    ) == {'test1': 'test', 'test2': 'test'}


def test_chain():
    assert config._chain(
        {'test1': 'test'},
        {'test2': 'test'}
    ) == {'test1': 'test', 'test2': 'test'}


config = Config(config_file)


def test_load_from_json_config():
    config.load()


def test_loaded_data_from_persistent():
    assert config.persistent['address'] == '127.0.0.1'
    assert config.persistent['port'] == 1234


def test_loaded_data_from_chainmap():
    assert config.data['address'] == '127.0.0.1'
    assert config.data['port'] == 1234


def test_override_empty_after_config_loaded():
    assert len(config.override) == 0


config = Config(config_file, [{'address': '0.0.0.0'}])


def test_load_from_json_config():
    config.load()


def test_loaded_data_from_override():
    assert config.override['address'] == '0.0.0.0'
    assert len(config.override) == 1


def test_loaded_data_from_persistent():
    assert config.persistent['port'] == 1234
    assert len(config.persistent) == 2


def test_loaded_data_from_chainmap():
    assert config.data['address'] == '0.0.0.0'
    assert config.data['port'] == 1234
