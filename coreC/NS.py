import uuid
import clips
import faker
from pyNamespace import Namespace
from .TPL import TPL
from .IMP import IMP

class NS(TPL, IMP):
    def __init__(self, *args, **kw):
        graphs = [ x.ns.value for x in args ]
        self.ns = Namespace(*graphs)
        IMP.__init__(self)
        TPL.__init__(self)
        for k in kw:
            self.ns.set(f"/etc/{k}", kw[k])
        self.get = self.ns.get
        self.set = self.ns.set
        self.mkdir = self.ns.mkdir
        self.rm = self.ns.rm
        self.o = self.ns.object
        self.ls = self.ns.ls
        self.Set("id", str(uuid.uuid4()))
        self.Set("faker", faker.Faker())
        self.Set("env", clips.Environment())
        self.Reload()
        self.Run = self.env.run
    def Set(self, name, value):
        setattr(self, name, value)
        self.set(f"/etc/{name}", value)
    def Reload(self):
        if hasattr(self, 'env') is True:
            env = getattr(self, 'env')
            env.clear()
            env.reset()
            IMP.Reload(self)
            TPL.Reload(self)
