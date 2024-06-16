from .strategy import Strategy
import os

class RectStrategy(Strategy):#具体产品1
    def __init__(self, icon_path):
        super().__init__(icon_path)
        try:
            width = int(os.getenv('WIDTH'))#从环境变量中读取矩形的宽度
        except Exception as e:
            width = 50#无有效设置时，默认宽度为50
        self.width = width
    
    def setPrefix(self,entry):
        super().setPrefix(entry)
        for parent in entry.parents:
            if entry.istail:
                self.prefix += '└──'
            else:
                self.prefix += '|──'
        if entry.isroot:
            self.prefix += '┌─'
        elif entry.istail:
            self.prefix += '└─'
        else:
            self.prefix += '├─'

    def setSuffix(self,entry):
        super().setSuffix(entry)
        length = len(self.getPrefix()+self.getEntryView(entry))
        if length < self.width:
            self.suffix += '─' * (self.width-1-length)
        if entry.isroot:
            self.suffix  += '┐'
        elif entry.istail:
            self.suffix  += '┘'
        else:
            self.suffix  += '|'
