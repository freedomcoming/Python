"""
比较两个dict
"""

class MyDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__dict__ = self
    def cmp(self, d1,d2):
        print(type(d1.keys()))
        print(type(d2.items()))
        return d1.keys() & d2.keys()
    
d = MyDict()
a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}

b = {
    'w' : 10,
    'x' : 11,
    'y' : 2
}
r = d.cmp(a,b)
print(r)