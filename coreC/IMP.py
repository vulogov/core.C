import os.path
import pkgutil
import importlib

class IMP(object):
    def __init__(self):
        pass
    def Reload(self):
        pass
    def __ImportModule(self, _module):
        _attrs = ['_lib', '_mkdir', '_set', '_tpl']
        _mod = {}
        for a in _attrs:
            if hasattr(_module, a) is True:
                _mod[a] = getattr(_module, a)
        return _mod
    def Import(self, module):
        for loader, module_name, is_pkg in pkgutil.walk_packages(importlib.import_module(module).__path__):
            _module = loader.find_module(module_name).load_module(module_name)
            _mod = self.__ImportModule(_module)