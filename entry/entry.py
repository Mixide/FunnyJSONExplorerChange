class Entry:#代表json中一个项
    def __init__(self):
        self.isroot = False
        self.isfirst = False
        self.isleaf = False
        self.islast = False
        self.istail = False
        self.parents = None
        self.sons = None
        self.level = None
        self.key = None
        self.value = None
    