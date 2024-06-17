from Strategy.TreeStrategy import TreeStrategy
from Strategy.RectStrategy import RectStrategy
from entry.analyzer import Analyzer
import argparse 

class FJE():
    def __init__(self,strategy):
        self.analyzer = Analyzer()
        self.strategy = strategy

    def setStrategy(self,strategy):
        self.strategy = strategy
        
    def _loadfile(self,json_path):
        self.json_path = json_path
    
    def isend(self):
        return self.analyzer.isend()
    
    def getNext(self):
        return self.analyzer.getNext()

    def show(self,json_path=None):
        if json_path != None:
            self._loadfile(json_path)
        self.analyzer.analyze(self.json_path)
        while not self.isend():
            entry = self.getNext()
            self.showSingle(entry)
    
    def showSingle(self,entry):
        print(self.strategy.execute(entry))


strategy_dic = {#策略哈希表
    'TREE': TreeStrategy,
    'RECT': RectStrategy
}
def selectStrategy(style,icon_path):#选择具体策略
    key = style.upper()
    return strategy_dic[key](icon_path)

def main():
    parser = argparse.ArgumentParser(description='Chose the style and icon and input the file path')
    parser.add_argument('-s', '--style',required=True,help='the output style')
    parser.add_argument('-i', '--icon',required=True,help='the path of the icon config')
    parser.add_argument('-f', '--file',required=True,help='the path of json file')
    args = parser.parse_args()
    style = args.style
    icon_path = args.icon
    file_path = args.file
    strategy = selectStrategy(style,icon_path)
    fje = FJE(strategy)
    fje.show(file_path)

if __name__ == '__main__':
    main()