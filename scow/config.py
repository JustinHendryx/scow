import json
import sys
from collections import ChainMap


class Config(object):
    def __init__(self, config_file=None, override_sources=None):
        self._config_file = config_file
        self._override_sources = override_sources
        self.persistent = {}
        self.override = {}
        self.data = {}

    def _merge(self, config_ref, config):
        return dict(**config_ref, **config)

    def _chain(self, *mappings):
        return ChainMap(*mappings)

    def _create(self):
        with open(self._config_file, 'x') as handle:
            json.dump({}, handle)

    def _merged_from_json_handle(self, handle):
        return self._merge(self.persistent, json.load(handle))

    def load(self):
        if self._config_file:
            try:
                with open(self._config_file, 'r') as handle:
                    self.persistent = self._merged_from_json_handle(handle)
            except IOError as err:
                raise Exception('Could not load config file') from err

        if self._override_sources:
            for source in self._override_sources:
                self.override = self._merge(self.override, source)

        self.data = self._chain(self.override, self.persistent)

    def save(self):
        if self.persistent:
            with open(self._config_file, 'w') as handle:
                json.dump(self.persistent, handle)


config = None
