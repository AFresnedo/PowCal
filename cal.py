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

#TODO change implementation of dates to something cleaner to use while traversing
class AppTree:
    "Tree beginning with a root, linking to month nodes, linking to day nodes, which are holding Day UDTs."
    def __init__(self):
        self.root = AppTreeMultiNode([-1111, -11, -11], None, None)
    
    #pre: date is a list of the form [4 digit int, 2 digit int, 2 digit int]
    #post: return reference to appropriate Day UDT
    def getDay(self, date):
        #base case, self is an AppTreeNode also known as an AppTree node that is holding a day date
        if self.child isInstance(Day()):
            return self.child
        #move onto child that matches and then call its getDay method to advance down the tree
        else:
            #current node is root
            if self.date[0] = -1111
                match = date[0]
                for c in self.child:
                    if self.child.date[0] is match:
                        self.child.getDay(date)
                        break
                else:
                    assert False #TODO change to exception of no match found
            #current node is year
            elif self.date[1] = -11
                match = date[1]
                for c in self.child:
                    if self.child.date[1] is match:
                        self.child.getDay(date)
                        break
                else:
                    assert False #TODO change to exception of no match found
            #current node is month
            elif self.date[2] = -11
                match = date[2]
                for c in self.child:
                    if self.child.date[2] is match:
                        self.child.getDay(date)
                        break
                else:
                    assert False #TODO change to exception of no match found
            else:
                assert False #TODO change to exception of no match found

    #post: adds Day UDT to tree
    def addDay(self, target = [-1111, -11, -11]):
        currentNode = traverseUntil(target)
        if currentNode.date == target:
            #day node already created, ensure day object holding hours exists
            assert isinstance(currentNode.child, day.Day)
            #raise exception since day already added
            raise day.PreventOverride()
        if currentNode[0] = -1111:
            #add year, month, and day to root
            yearNode = AppTreeMultiNode(self, [target[0], -11, -11])
            self.childL.append(
        elif currentNode.date[1] = -11:
            None #add month and day to existing year
        elif currentNode.date[2] = -11:
            None #add day to existing month
        else:
            assert False

    #pre: target is a valid date
    #post: returns node if found, otherwise the last node on the partial path to where it would be
    def traverseUntil(self, target = [-1111, -11, -11]):
        #check preconditions
        #base case
        if self.date = target:
            return self
        #reached end of complete tree branch without finding target: algorithm or structural error
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
            #goto next target, else return self because child doesn't exist
            for c in self.childL: 
                if c.date == nextTarget:
                    c.traverseTo(target)
                    break
            else:
                return self

class AppTreeNode:
    "A day in AppTree holding its date and its links."
    def __init__(self, date = [-1111, -11, -11], parent = None, child = None):
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
    def __init__(self, date = [-1111, -11, -11], parent = None, child = None):
        self.parent = parent
        self.date = date
        self.child = [child]

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
