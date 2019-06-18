# coding: utf-8
import types
import weakref

class CAction:
    pass

class CRecord:

    def __init__ (self):
        self.m_ClsOriNew = {}
        self.m_ClsOriGetAttr = {}
        self.m_ClsCnt = []
        self.m_ObjInfo = {}
    
    def Record(self, cls, *args, **kwargs):
        self.m_ClsOriNew[cls] = cls.__new__
        cls.__new__ = self._NewClsNew
        return cls
    
    def _ClsNew(self, cls, *args, **kwargs):
        print("cls is run __new__", cls.__name__)
        obj = self.m_ClsOriNew[cls](cls, *args, **kwargs)
        self.m_ClsCnt[cls].append(weakref.ref(obj))  # 还有序列化信息要记录
        
        return obj
    
    def _Obj__getattr__(self, name):
        return None
    
    def __get__(self, instance, cls):
        print("__get__", self, instance, cls)
        if not instance:
            return self
        return instance

rec = CRecord()

@rec.Record
class Test:

    def __init__(self):
        self.m_A = 100
    
    def ListenParam():
        return ["m_A", ]

a = Test()
print(a.m_A)


