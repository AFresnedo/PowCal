"""
Module for running unit tests for PowCal project. Currently only covering day.py module.
"""

import unittest #python's unit test standard
import day #to perform unit tests on

class DayTestCase(unittest.TestCase):
    def setUp(self):
        #create day objects
        self.dayBlank = day.Day()
        self.dayHalfFull = day.Day()
        self.dayFull = day.Day()
        self.dayDup = day.Day()

        #populate half full day
        for i in range(24):
            self.dayHalfFull.sch[i] = 'firstJobInterview_00h0q_05h3q'
        for i in range(48, 73):
            self.dayHalfFull.sch[i] = 'programming_12h0q_18h0q'

        #populate full day
        for i in range(24):
            self.dayFull.sch[i] = 'firstJobInterview_00h0q_05h3q'
        for i in range(24, 48):
            self.dayFull.sch[i] = 'videoGamesFull_06h0q_11h3q'
        for i in range(48, 73):
            self.dayFull.sch[i] = 'programming_12h0q_18h0q'
        for i in range(73, 96):
            self.dayFull.sch[i] = 'sleep_18h1q_23h3q'

        #populate dup day
        for i in range(24):
            self.dayDup.sch[i] = 'videoGamesDup_00h0q_05h3q'
        for i in range(48, 73):
            self.dayDup.sch[i] = 'videoGamesDup_12h0q_18h0q'

    def test_init(self):
        #check values of blank schedule
        for e in self.dayBlank.sch:
            self.assertEqual(e, 'noAppointment_00h0q_23h3q')
        #verify proper list sizes
        self.assertEqual(len(self.dayBlank.sch), 96)
        self.assertEqual(len(self.dayHalfFull.sch), 96)
        self.assertEqual(len(self.dayFull.sch), 96)

    def test_add(self):
        self.dayBlank.add('freeDay', '_00h0q', '_23h3q')
        #test indicies and values all written properly
        for i in range(0, len(self.dayBlank.sch)):
            self.assertEqual(self.dayBlank.sch[i], 'freeDay_00h0q_23h3q')
        self.dayBlank.add('broken', '_00h0q', '_23h3q')
        self.dayBlank.add('beginning', '_00h0q', '_00h0q')
        self.dayBlank.add('end', '_23h3q', '_23h3q')
        self.dayBlank.add('middle', '_12h0q', '_12h0q')

        #write into empty slots until conflict with programming_12h0q_18h
        self.dayHalfFull.add('freeDay', '_10h0q', '_14h2q')
        #commented out print lines for cleanliness in code running, but they are useful
        #print(self.dayHalfFull.sch[self.dayHalfFull.conToInd('_10h0q')])
        #print(self.dayHalfFull.sch[self.dayHalfFull.conToInd('11h3q')])
        #print(self.dayHalfFull.sch[self.dayHalfFull.conToInd('12h0q')])

    def test_delApp(self):
        #clear a schedule
        self.dayHalfFull.delApp('firstJobInterview')
        self.dayHalfFull.delApp('programming')
        for e in self.dayHalfFull.sch:
            assert e == 'noAppointment_00h0q_23h3q'

        #check for false positive
        self.dayFull.delApp('videoGames')
        for e in self.dayFull.sch:
            assert e != 'noAppointment_00h0q_23h3q'


    def test_getTime(self):
        #test blank
        matches = self.dayBlank.getTime('noAppointment')
        self.assertEqual(1, len(matches)) #verify only 1 match returned
        self.assertEqual('noAppointment_00h0q_23h3q', matches[0])
        
        #test halfFull
        matches = self.dayHalfFull.getTime('firstJobInterview')
        self.assertEqual(1, len(matches))
        self.assertEqual('firstJobInterview_00h0q_05h3q', matches[0])

        #test dup
        matches = self.dayDup.getTime('videoGamesDup')
        self.assertEqual(2, len(matches))
        self.assertEqual('videoGamesDup_00h0q_05h3q', matches[0])
        self.assertEqual('videoGamesDup_12h0q_18h0q', matches[1])

        #test false positives from pattern
        matches = self.dayFull.getTime('first')
        self.assertEqual(1, len(matches))
        self.assertEqual('noAppointment_00h0q_23h3q', matches[0])


    def test_getName(self):
       self.assertEqual(self.dayBlank.getName('_05h3q'), 'noAppointment_00h0q_23h3q')

       self.assertEqual(self.dayFull.getName('_00h0q'), 'firstJobInterview_00h0q_05h3q')
       self.assertEqual(self.dayFull.getName('_05h3q'), 'firstJobInterview_00h0q_05h3q')
       self.assertEqual(self.dayFull.getName('_06h1q'), 'videoGamesFull_06h0q_11h3q')
       self.assertEqual(self.dayFull.getName('_16h3q'), 'programming_12h0q_18h0q')
       self.assertEqual(self.dayFull.getName('_23h3q'), 'sleep_18h1q_23h3q')

#TODO consider a good design way to ensure assert is intentionally triggered to succeed a test
class VerStrFormTestCase(unittest.TestCase):
    def setUp(self):
        self.blankString = 'noAppointment_00h0q_23h3q'
        self.testString = 'pythonLearning_06h0q_09h2q'
        self.brokenString = '0break'
        self.wrongTime = 'wrongTime_03h2q_34h1q'

    def test_verStrForm(self):
        day.verStrForm(self.blankString)
        day.verStrForm(self.testString)
        #following tests will trigger assert as intended if decommented
        #day.verStrForm(self.brokenString) 
        #day.verStrForm(self.wrongTime)
