from abc import ABC, abstractmethod
import json
class Strategy(ABC):
    def __init__(self,icon_path):
        self._loadicon(icon_path)

    def _loadicon(self,icon_path):
        with open(icon_path,'r',encoding='utf-8') as icon_file:
            icon_data = json.load(icon_file)
            self.leaf_icon = icon_data['leaf']
            self.norm_icon = icon_data['non-leaf']

    def getPrefix(self):
        return self.prefix
    
    def getSuffix(self):
        return self.suffix
    
    def getEntryView(self,entry):
        if entry.isleaf:
            icon = self.leaf_icon
        else:
            icon = self.norm_icon
        if entry.isleaf and entry.value != '':
            return icon + entry.key+':'+entry.value
        return icon + entry.key
    
    def execute(self,entry):
        self.setPrefix(entry)
        self.setSuffix(entry)
        return self.getPrefix()+self.getEntryView(entry)+self.getSuffix()
    
    @abstractmethod
    def setPrefix(self,entry):
        self.prefix = ""
    
    @abstractmethod
    def setSuffix(self,entry):
        self.suffix = ""