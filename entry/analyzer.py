import json
from .entryBuilder import EntryBuilder
class Analyzer:#json结构分析器，提供迭代器接口
    def clean(self):
        self.list = []
        self.idx = 0

    def __init__(self):
        self.clean()

    def preOrder_analyze(self,item, idx, siz, level,parents):
        key,value = item
        rootFlag = len(self.list) == 0
        firstFlag = idx == 0
        lastFlag = idx == siz - 1
        leafFlag = not isinstance(value, dict)
        builder = EntryBuilder()
        entry = builder.setroot(rootFlag).setfirst(firstFlag).setlast(lastFlag).setleaf(leafFlag)\
            .setkey(key).setvalue(value).setlevel(level).setparents(parents).build()
        self.list.append(entry)
        parents.append(self.list[-1])
        sons = []
        if(isinstance(value, dict)):
            for new_idx,new_item in enumerate(value.items()):
                sons.append(len(self.list))
                self.preOrder_analyze(new_item,new_idx,len(value),level+1,parents)
        builder.setsons([self.list[s_i] for s_i in sons])
        parents.pop()

    def analyze(self,json_path):
        with open(json_path,'r') as json_file:
            root = json.load(json_file)
        self.clean()
        for idx, item in enumerate(root.items()):
            self.preOrder_analyze(item,idx,len(root),0,[])
        if len(self.list) > 0:
            self.list[-1].istail = True

    def getNext(self):
        result = self.list[self.idx]
        self.idx += 1
        return result

    def isend(self):
        return self.idx == len(self.list)