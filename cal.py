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
        appTable = appTable()
        appTree = appTree(2016)

    def append(self, time = -1.00):
        None #add information to an appointment to allow for double+ booking or fixing

#TODO i'm thinking appTreeNode and appTreeMultiNode
class appTree:
    "Tree beginning with a year root, holding month nodes, holding day nodes, holding Day UDT."
    def __init__(self, year = 2016):
        self.year = 2016
        self.root = appTreeDay('year', year)
    
    #post: return reference to appropriate Day UDT
    def getDay(self, date):
        None

    def trav(self, node, date):
        None

    #post: adds Day UDT to tree
    def addDay(self):
        None
        #recursive?
        #check for month: goto or add and goto
        #check for day: goto or add and goto
        #is this method too damn big? trying to do too much? yes, absolutely! needs to use
        #   methods that will be used by calendar for information like "does this month have any
        #   appointments scheduled?" stuff like checking strucutre should not be done here

class appTreeNode:
    "A day in appTree holding its date and its links."
    def __init__(self, parent = None, date = -1, child = None):
        self.parent = parent
        self.date = date
        self.child = day.Day()
    
    #TODO: determine if pass by reference is what is wanted here...depends if I want client to have
    #   access to interworking of the tree from just getting a parent of a node, make this class
    #   private? that avoids issues since it's okay for appTree to manipulate nodes
    #post: returns ref to month node
    def getParent(self):
        return self.month

    def getSelf(self):
        return self.day
    
    def getChild(self):
        return self.child

class appTreeMultiNode(appTreeNode):
    "The root, a year, or a month in appTree holding their dates and links."
    def __init__(self, parent = None, date = -1, child = None):
        None
    def getDay(self, day = -1):
        #TODO asserts, nicer if/else and return
        for d in self.dayL:
            if d.getDay is day:
                return d
            else:
                return -1
    
#hash based on unique year/month/day...and starting hour?
class appTable:
    def __init__(self):
        None

class appInfo:
    None
