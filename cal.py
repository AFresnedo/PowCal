"""
This module is intended to manage a calendar using Day UDTs. The calendar is designed to provide
enough information to the client to answer most questions a human could ask and answer of a calendar
full of appointments.

Created by AFresnedo for use with the Day module and Pow module in the PowCal project.
"""

#TODO check singleton and python
class Cal:
    "A singleton calendar storing appointments and their info for a client to view and manipulate."
    def __init__(self, year = 2016):
        appTable = AppTable()
        appTree = AppTree(2016)

    def append(self, time = -1.00):
        None #add information to an appointment to allow for double+ booking or fixing

class AppTree:
    "Tree beginning with a root, linking to month nodes, linking to day nodes, which are holding Day UDTs."
    def __init__(self):
        self.root = AppTreeMultiNode(None, None, None, root)
    
    #pre: date is a list of the form [4 digit int, 2 digit int, 2 digit int]
    #post: return reference to appropriate Day UDT
    def getDay(self, date):
        #base case, self is an AppTreeNode also known as an AppTree node that is holding a day date
        if self.child isInstance(Day()):
            return self.child
        #move onto child that matches and then call its getDay method to advance down the tree
        else:
            nodeType = self.ident
            if nodeType is root:
                match = date[0]
                for c in self.child:
                    if self.child.date is match:
                        self.child.getDay(date)
            elif nodeType is year:
                match = date[1]
                for c in self.child:
                    if self.child.date is match:
                        self.child.getDay(date)
            elif nodeType is month:
                match = date[2]
                for c in self.child:
                    if self.child.date is match:
                        self.child.getDay(date)
            else:
                assert(False) #TODO change to exception of no match found

    #post: adds Day UDT to tree
    def addDay(self):
        None
        #recursive?
        #check for month: goto or add and goto
        #check for day: goto or add and goto
        #is this method too damn big? trying to do too much? yes, absolutely! needs to use
        #   methods that will be used by calendar for information like "does this month have any
        #   appointments scheduled?" stuff like checking strucutre should not be done here

    #pre: target is a valid date
    #post: returns node if found, otherwise exception is thrown
    def traverseTo(self, target = [-1111, -11, -11]):
        #check preconditions
        #base case
        if self.date = target:
            return self
        #target doesn't exist, raise TargetNotFound
        elif self.child is None: #end of tree branch, no leaf
            raise Exception()
        #reached end of tree without finding target, traversal or structural error
        elif isinstance(self.child, day.Day): 
            assert False
        #move to next node on way to target
        else:
            nextTarget = []
            #determine how far traveled
            i = 0
            while self.date[i] == target[i]:
                nextTarget.append[target[i]]
                i+=1 
            nextTarget.append[target[i]]
            #complete identify of next target
            while 0 < i < 3:
                nextTarget.append[-11]
                i+=1
            #goto next target
            for c in self.childL: 
                if c.date == nextTarget:
                    c.traverseTo(target)
                    break
            else:
                assert False

    #post: returns smallest time unit of target's branch
    def traverseUntil(self, target = [-1111, -11, -11]):
        None

class AppTreeNode:
    "A day in AppTree holding its date and its links."
    def __init__(self, parent = None, date = [-1111, -11, -11], child = None):
        self.parent = parent
        self.date = date
        self.child = day.Day()
    
    #TODO: determine if pass by reference is what is wanted here...depends if I want client to have
    #   access to interworking of the tree from just getting a parent of a node, make this class
    #   private? that avoids issues since it's okay for AppTree to manipulate nodes
    #post: returns ref to month node
    def getParent(self):
        return self.parent

    def getSelf(self):
        return self.date
    
    def getChild(self):
        return self.child

class AppTreeMultiNode(AppTreeNode):
    "The root, a year, or a month in AppTree holding their dates and links."
    def __init__(self, parent = None, date = [-1111, -11, -11], child = None, ident = ident):
        self.parent = parent
        self.date = date
        self.child = [child]
        self.ident = ident

    def getChild(self):
        assert(False)
        None

    def getChild(self, date = -1):
        #TODO asserts, nicer if/else and return
        for c in self.child:
            if c.getSelf is date:
                return c
            else:
                return -1

    def addChild(self, date = -1):
        #TODO assert child doesn't exist already and date is valid
        #create all of child's links
        self.child.append(child)
    
#hash based on unique year/month/day...and starting hour?
class AppTable:
    def __init__(self):
        None

class AppInfo:
    None
