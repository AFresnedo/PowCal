"""
Module for running unit tests for cal.py in the PowCal project.
"""

import unittest #python's unit test library
import dataStruc #to perform unit tests on
import day

class DataStrucTestCase(unittest.TestCase):
    def setUp(self):
        #create empty tree
        self.emptyT = dataStruc.AppTree()
        #create tree with a single date
        self.oneT = dataStruc.AppTree()
        self.oneT.addDay(2016, 07, 31)
        #create tree with a single date and afterwards a Day obj attached to it
        self.twoT = dataStruc.AppTree()
        self.twoT.addDay(2016, 07, 31)
        self.twoT.addHrs(2016, 07, 31)
        
    def test_add(self):
        self.emptyT.addDay(2016, 07, 31)

    def test_get(self):
        dayOne = self.oneT.getDay(2016, 07, 31)
        print dayOne.date
        #check dayTwo is a Day obj
        dayTwo = self.twoT.getHrs(2016, 07, 31)
        assert isinstance(dayTwo, day.Day)
