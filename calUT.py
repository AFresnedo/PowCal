"""
Module for running unit tests for cal.py in the PowCal project.
"""

import unittest #python's unit test library
import cal #to perform unit tests on

class CalTestCase(unittest.TestCase):
    def setUp(self):
        #create empty tree
        self.emptyT = cal.AppTree()
        #create tree with a single date
        self.oneT = cal.AppTree()
        self.oneT.addDay([2016, 07, 31])
        
    def test_add(self):
        self.emptyT.addDay([2016, 07, 11])

    def test_get(self):
        dayOne = self.oneT.getDay([2016, 07, 31])
