import re
from yaml import load, FullLoader
from collections.abc import Mapping

class Content(Mapping):
    
    __delimiter = "^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimiter, re.MULTILINE)

    
    def load(self, cls, string):
        
        _, fm, content = self.__regex.split(string, 2)
        
        load(fm, Loader=FullLoader)
        cls(metadata, content)
    
        
    def __init__(self, metadata, content) -> None:
        super().__init__()
        self.data = metadata
        self.data.update({ "content": content })
    
    
    @property
    def body(self):
        return self.data["content"]
    
    
    @property
    def type(self):
        return self.data["type"] if self.data["type"] else None
    
    
    @type.setter
    def type(self, value):
        self.data["type"] = value
    
        
    def __getitem__(self, __key: _KT) -> _VT_co:
        return self.data(__key)
    

    def __iter__(self) -> Iterator[_T_co]:
        return self.data.__iter__()
    
    
    def __len__(self) -> int:
        return self.data.__len__()
    
    
    def __repr__(self) -> str:
        for key, value in self.data.items():
            if key is not "content":
                data[key] = value
        
        return str(self.data)