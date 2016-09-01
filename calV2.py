class AppTreeNode:
    "A node holding a date in AppTree."
    def __init__(self, date = [-1111, -11, -11], child = []):
        self.date = date
        self.child = child

class AppTree:
    "A tree holding AppTreeNodes."
    def __init__(self):
        self.root = AppTreeNode()
    
    def addYear(self, year):
        date = [year, -11, -11]
        for c in self.root.child:
            if c.date == date:
                assert False #TODO change to raise exception
        self.root.child.append(AppTreeNode(date))

    def addMonth(self, year, month):
        date = [year, month, -11]
        self.addYear(year)
        yearNode = self.getYear(year)
        yearNode.child.append(AppTreeNode(date))

    def addDay(self, year, month, day):
        date = [year, month, day]
        self.addYear(year)
        self.addMonth(year, month)
        monthNode = self.getMonth(year, month)
        monthNode.child.append(AppTreeNode(date))

    def getYear(self, year):
        date = [year, -11, -11]
        for c in self.root.child:
            if c.date == date:
                return c

    def getMonth(self, year, month):
        date = [year, month, -11]
        yearNode = self.getYear(year)
        for c in yearNode.child:
            if c.date == date:
                return c

    def getDay(self, year, month):
        date = [year, month, day]
        monthNode = self.getMonth(year, month)
        for c in monthNode.child:
            if c.date == date:
                return c
