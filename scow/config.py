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

    def load(self):
        if self._config_file:
            try:
                with open(self._config_file, 'r') as handle:
                    data = json.load(handle)
                    self.persistent = self._merge(self.persistent, data)
            except FileNotFoundError:
                open(self._config_file, 'x').close()
                self.load()
            except IOError as err:
                print(err)
                sys.exit(1)

        if self._override_sources:
            for source in self._override_sources:
                self.override = self._merge(self.override, source)

        self.data = self._chain(self.override, self.persistent)

    def save(self):
        if self.persistent:
            with open(self._config_file, 'wx') as handle:
                json.dump(self.persistent, handle)


config = None
