from .strategy import Strategy

class TreeStrategy(Strategy):#具体产品2
    def __init__(self, icon_path):
        super().__init__(icon_path)

    def setPrefix(self,entry):
        super().setPrefix(entry)
        for parent in entry.parents:
            if not parent.islast:
                self.prefix += '|  '
            else:
                self.prefix += '   '
        if entry.islast:
            self.prefix += '└─'
        else:
            self.prefix += '├─'
    
    def setSuffix(self,entry):
        super().setSuffix(entry)

        