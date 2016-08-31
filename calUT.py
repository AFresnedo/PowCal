"""
Module for running unit tests for cal.py in the PowCal project.
"""

import unittest #python's unit test library
import cal #to perform unit tests on

class CalTestCase(unittest.TestCase):
    def setUp(self):
        #create empty tree
        self.emptyT = cal.AppTree()
        
    def test_add(self):
        self.emptyT.addDay([2016, 07, 11])
