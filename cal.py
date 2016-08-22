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

class appTree:
    "Tree beginning with a year root, holding month nodes, holding day nodes, holding Day UDT."
    def __init__(self, year = 2016):
        self.year = 2016
        self.root = appTreeNode('year', year)
    
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
    "A node in appTree holding the year, month, xor day."
    #pre: parent (year or month) node and date to hold
    #post: creates node holding date and linked to parent
    def __init__(self, ident = '', date = -1, parent = None):
        self.ident = ident #TODO asserts to only allow 'year', 'month', xor 'day'
        self.date = date #TODO asserts for valid number
        self.parent = parent #TODO asserts to properly structure
        self.children = None
    
    #TODO: determine if pass by reference is what is wanted here...depends if I want client to have
    #   access to interworking of the tree from just getting a parent of a node, make this class
    #   private? that avoids issues since it's okay for appTree to manipulate nodes
    #pre: self.node not a year
    #post: returns parent
    def getParent(self):
        assert self.ident is not 'year' #TODO make sure this is proper, instead of !=
        return self.parent
    
    #post: returns child if exists, otherwise returns None
    def getChild(self):
        return self.child

    #pre: a month node if self.node is a year, day node if self.node is a month, otherwise Day UDT
    #post: sets arg as child for self.node
    def addChild(self, child = None):
        assert child is not None
        if self.ident is 'year':
            assert child.ident is 'month'
        if self.ident is 'month':
            assert child.ident is 'day'
        if self.ident is 'day':
            #assert child.ident is a Day #TODO 
            None
        for c in self.children:
            if child == c:
                None #TODO will break get me out of the for loop? that would be nice


#hash based on unique year/month/day...and starting hour?
class appTable:
    def __init__(self):
        None

class appInfo:
    None
