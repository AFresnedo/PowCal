"""
Module for running unit tests for dataStruc.py in the PowCal project.
"""

import unittest #python's unit test library
import dataStruc #to perform unit tests on
import day

class AppTreeTestCase(unittest.TestCase):
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

class AppMapTestCase(unittest.TestCase):
    def setUp(self):
        #create empty map
        self.emptyM = dataStruc.AppMap()

        #create map with one appointment
        self.oneM = dataStruc.AppMap()
        self.oneM.addApp('dentist_12h0q_14h0q_01_09_9999')

    def tearDown(self):
        self.oneM.delApp('dentist_12h0q_14h0q_01_09_9999')

    def test_add(self):
        self.emptyM.addApp('noAppointment_00h0q_23h3q_31_12_9999')
        for key in self.emptyM.appDict:
            print key
            print self.emptyM.appDict[key]
        self.emptyM.delApp('noAppointment_00h0q_23h3q_31_12_9999')

    def test_getAppInfo(self):
        print self.oneM.getAppInfo('dentist_12h0q_14h0q_01_09_9999')
