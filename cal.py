"""
This module is intended to manage a calendar using Day UDTs. The calendar is designed to provide
enough information to the client to answer most questions a human could ask and answer of a calendar
full of appointments.

Created by AFresnedo for use with the Day module and Pow module in the PowCal project.
"""

import day

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
        self.root = AppTreeMultiNode([-1111, -11, -11], None)
    
    #pre: date is a list of the form [4 digit int, 2 digit int, 2 digit int]
    #post: return reference to appropriate Day UDT
    def getDay(self, date, node = None):
        if node is None:
            node = self.root
        #base case, current node is day
        if isinstance(node.child, day.Day):
            return node.child
        #move onto child that matches and then call its getDay method to advance down the tree
        else:
            if node.date[0] == -1111:
                #current node is root
                match = date[0]
                for c in node.child:
                    if c.date[0] is match:
                        node.child.getDay(date)
                        break
                else:
                    assert False #TODO change to exception of no match found
            elif node.date[1] == -11:
                #current node is year
                match = date[1]
                for c in node.child:
                    if c.date[1] is match:
                        node.child.getDay(date)
                        break
                else:
                    assert False #TODO change to exception of no match found
            elif node.date[2] == -11:
                #current node is month
                match = date[2]
                for c in node.child:
                    if node.child.date[2] is match:
                        node.child.getDay(date)
                        break
                else:
                    assert False #TODO change to exception of no match found
            else:
                assert False #TODO change to exception of no match found

    #post: adds Day UDT to tree
    def addDay(self, target = [-1111, -11, -11]):
        #go as far down appropriate branch as possible
        currentNode = self.traverseUntil(target)
        #check if it is correct to add day to this branch
        if currentNode.date == target:
            #day node already created, ensure day object holding hours exists
            assert isinstance(currentNode.child, day.Day)
            #raise exception since day already added
            raise day.PreventOverride()
        #TODO refactor
        #add leaf to tree, creating missing nodes in branch as needed
        if currentNode.date[0] == -1111:
            #add year, month, and day to root 
            dayNode = AppTreeMultiNode([target[0], target[1], target[2]])
            monthNode = AppTreeMultiNode([target[0], target[1], -11], dayNode)
            yearNode = AppTreeMultiNode([target[0], -11, -11], monthNode)
            currentNode.child.append(yearNode)
        elif currentNode.date[1] == -11:
            #add month and day to existing year
            dayNode = AppTreeMultiNode([target[0], target[1], target[2]])
            monthNode = AppTreeMultiNode([target[0], target[1], -11], dayNode)
            currentNode.child.append(monthNode)
        elif currentNode.date[2] == -11:
            #add day to existing month
            dayNode = AppTreeMultiNode([target[0], target[1], target[2]])
            currentNode.child.append(dayNode)
        else:
            assert False

    #pre: target is a valid date
    #post: returns node if found, otherwise the last node on the partial path to where it would be
    def traverseUntil(self, target = [-1111, -11, -11], node = None):
        #TODO investigate why this doesn't work as a parameter
        if node is None:
            node = self.root
        #check preconditions
        #base case
        if (node.date == target or node.child is None or node.child == [None]):
            return node
        #check if reached end of complete tree branch without finding target: algorithm or structural error
        elif isinstance(node.child, day.Day): 
            assert False
        #move to next node on way to target
        else:
            nextTarget = []
            #determine how far traveled
            i = 0
            while node.date[i] == target[i]:
                nextTarget.append(target[i])
                i+=1 
            nextTarget.append(target[i])
            #complete identify of next target
            while 0 < i < 3:
                nextTarget.append(-11)
                i+=1
            #goto next target, else return node because child doesn't exist
            for c in node.child: 
                if c.date == nextTarget:
                    c.traverseTo(target)
                    break
            else:
                return node

class AppTreeNode:
    "A day in AppTree holding its date and its links."
    def __init__(self, date = [-1111, -11, -11], child = None):
        self.date = date
        self.child = day.Day()
    
    def getSelf(self):
        return self.date
    
    def getChild(self):
        return self.child

class AppTreeMultiNode(AppTreeNode):
    "The root, a year, or a month in AppTree holding their dates and links."
    def __init__(self, date = [-1111, -11, -11], child = None):
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
