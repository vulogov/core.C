import os.path
import pkgutil
import importlib
import functools

class IMP:
    def __init__(self):
        pass
    def Reload(self):
        _mods = IMP.Import(self, 'coreC.stdlib')
        for i in ['ImportMkdirs', 'ImportTemplates', 'ImportSet', 'ImportLib']:
            self.ImportRun(_mods, i)
    def __ImportModule(self, _module):
        _attrs = ['_lib', '_mkdir', '_set', '_tpl']
        _mod = {}
        for a in _attrs:
            if hasattr(_module, a) is True:
                _mod[a] = getattr(_module, a)
        return _mod
    def Import(self, module):
        _m = []
        for loader, module_name, is_pkg in pkgutil.walk_packages(importlib.import_module(module).__path__):
            _module = loader.find_module(module_name).load_module(module_name)
            _mod = self.__ImportModule(_module)
            _m.append(_mod)
        return _m
    def ImportRun(self, _mods, _fun):
        if hasattr(self, _fun) is True:
            _f = getattr(self, _fun)
            for i in _mods:
                _f(i)
    def ImportMkdirs(self, _mod):
        if "_mkdir" in _mod:
            for m in _mod["_mkdir"]:
                self.ns.rm(m)
                self.ns.mkdir(m)
    def ImportTemplates(self, _mod):
        if "_tpl" in _mod:
            for k in _mod["_tpl"]:
                v = _mod["_tpl"][k]
                self.ns.set(f"/templates/{k}", v)
    def ImportSet(self, _mod):
        if "_set" in _mod:
            for k in _mod["_set"]:
                self.ns.rm(k)
                self.ns.set(k, _mod["_set"][k])
    def ImportLib(self, _mod):
        if "_lib" in _mod:
            for k in _mod["_lib"]:
                v = _mod["_lib"][k]
                if callable(v) is True:
                    self.ns.rm(k)
                    self.ns.set(k, functools.partial(v, self))
