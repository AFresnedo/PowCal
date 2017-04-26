"""
This module is designed to store appointments for the cal module in both tree
and hashtable formats.

Created by AFresnedo for use with the Day module and Cal module in the PowCal
project.
"""

import day #for Day object, holds appointments
import os #for deleting files

"""
Tree Data Structure
"""

class AppTreeNode:
    "A node holding a date in AppTree."
    def __init__(self, date = [-1111, -11, -11], child = []):
        self.date = date
        self.child = child

# TODO looks like no precondition for nodes already existing
class AppTree:
    "A tree holding AppTreeNodes."
    def __init__(self):
        self.root = AppTreeNode()

    def addYear(self, year):
        date = [year, -11, -11]
        toAdd = AppTreeNode(date)
        self.safeAdd(self.root, toAdd, date)

    def addMonth(self, year, month):
        date = [year, month, -11]
        self.addYear(year)
        yearNode = self.getYear(year)
        toAdd = AppTreeNode(date)
        self.safeAdd(yearNode, toAdd, date)

    def addDay(self, year, month, d):
        date = [year, month, d]
        self.addYear(year)
        self.addMonth(year, month)
        monthNode = self.getMonth(year, month)
        toAdd = AppTreeNode(date)
        self.safeAdd(monthNode, toAdd, date)

    def addHrs(self, year, month, d):
        date = [year, month, d]
        self.addYear(year)
        self.addMonth(year, month)
        self.addDay(year, month, d)
        dayNode = self.getDay(year, month, d)
        dayNode.child = day.Day()

    def getYear(self, year):
        date = [year, -11, -11]
        for c in self.root.child:
            if c.date == date:
                return c
        else:
            assert False #TODO exception

    def getMonth(self, year, month):
        date = [year, month, -11]
        yearNode = self.getYear(year)
        for c in yearNode.child:
            if c.date == date:
                return c
        else:
            assert False #TODO exception

    def getDay(self, year, month, d):
        date = [year, month, d]
        monthNode = self.getMonth(year, month)
        for c in monthNode.child:
            if c.date == date:
                return c
        else:
            assert False #TODO exception

    def getHrs(self, year, month, d):
        date = [year, month, d]
        dayNode = self.getDay(year, month, d)
        return dayNode.child

    def safeAdd(self, parent, toAdd, date):
        add = True
        for c in parent.child:
            if c.date == date:
                add = False
        if add:
            parent.child.append(toAdd)

"""
Map Data Structure
"""

class AppMap():
    "A class storing (key, val) pairs of (appointment date, unique text file)."
    def __init__(self):
        self.appDict = {}

    #key format: noAppointment_00h0q_23h3q_31_12_9999
    def addApp(self, key):
        f = self.createFile(key)
        self.appDict[key] = f

    def getAppInfo(self, key):
        return self.appDict[key]

    def delApp(self, key):
        os.remove(key + '.txt')
        del self.appDict[key]

    def createFile(self, key):
        f = open(key + '.txt', 'a')
        #TODO fill in the blanks using the key
        f.write('Appointment name:\n')
        f.write('Date:\n')
        f.write('Start time:\n')
        f.write('End time:\n')
        f.write('Type:\n')
        f.close()
        return f

"""
Shared Resources
"""
class DateNotFound(Exception):
    None
