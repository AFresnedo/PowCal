"""
This module is designed to store scheduling appointments over the course of one <full> day in
<quarter hour> intervals. The object created is able to accept an appointment with a start time and
end time. If the appointment given does not conflict with another appointment it will be stored,
otherwise it will instead return the name of the conflicting appointment. A function is also
provided to convert from string to index. In this module's first iteration a
appointmentName_hourNumber_quarterHourNumber string is used for all operations and must be used
correctly by the client.

A note on the special string format, the last time value indicates the start of the final quarter
hour of the appointment.

Created by AFresnedo for use with the PowCal Calendar module
"""

import re #for regex used in storing appointments

class Day:
    "A class storing appointments for one day."
    noApp = 'noAppointment_00h0q_23h3q' #time duration is not accurate unless no apps in day
    def __init__(self):
        self.sch = [Day.noApp for i in range(96)] #create array of 96 quarter hours

    def add(self, appName = 'noAppointment', start = '_00h0q', end = '_23h3q'):
        verStrForm(appName + start + end) #verify string format
        firstIndex = self.conToInd(start)
        lastIndex = self.conToInd(end) 
        #schedule appointment, throw exception if it will override an appointment
        try:
            indexReached = -1 #for except
            for i in range(firstIndex, lastIndex + 1):
                #throw exception if an appointment is about to be overriden
                if self.sch[i] != Day.noApp:
                    raise PreventOverride(appName + start + end, self.sch[i])
                #schedule appointment in the quarter hour indexed by i
                self.sch[i] = appName + start + end
                indexReached = i 
        except:
            #clear appointment times scheduled incorrectly (because of override)
            for i in range(firstIndex, indexReached + 1):
                self.sch[i] = Day.noApp

    #pre: name of appointment(s), default returns open times
    #post: returns list of strings of appointment(s) in name+start+end format
    def getTime(self, appName = 'noAppointment'):
        #check precondition
        verNameForm(appName)
        #get list of appointments with the passed name
        listApp = []
        p = re.compile(appName + '_') #'_' to force whole word match
        lastMatch = Day.noApp
        for e in self.sch:
            if (p.match(e)):
                if e != lastMatch:
                    lastMatch = e
                    listApp.append(e) 

        #check for empty list before returning
        if listApp == []:
            listApp = [Day.noApp]
        
        #pass format test(s) and return
        for e in listApp:
            verStrForm(e)
        return listApp

    #pre: time of appointment in special string format
    #post: returns full special string of appointment including name+start+end
    def getName(self, time = ''):
        #check precondition
        verTimeForm(time)
        #get string
        index = self.conToInd(time)
        string = self.sch[index]
        #pass string format test and return
        verStrForm(string)
        return string

    #pre: name of appointment
    #post: removes all appointments scheduled with that name
    def delApp(self, appName = ''):
        #check precondition
        verNameForm(appName)
        #replace all matches with noApp string
        p = re.compile(appName + '_')
        for i in range(0, len(self.sch) - 1):
            if p.match(self.sch[i]):
                self.sch[i] = 'noAppointment_00h0q_23h3q'

    #TODO this requires some interpretation of the string
    def clearTime(self, time = '_24h1q'):
        None

    #pre: a valid time in proper format
    #post: returns corresponding index
    def conToInd(self, time = ''):
        "A method to convert the string version of a start or end time to an index for Day's list."
        #check precondition
        verTimeForm(time)
        #extract number of hours and number of quarter hours
        p = re.compile('\d+') 
        values = p.findall(time) #get 2 element list [hour, quarter]
        index = 4*int(values[0]) + int(values[1]) #calculate index using hour and quarter
        assert 0<=index<len(self.sch)
        return index

'''
Helper Functions
'''

#current implementation of UDT Day requires interval to be a multiple of 0.25
tStep = 0.25 #smallest unit of time is a quarter hour written as 0.25

#pre: appName is a single word, start and end are multiples of tStep
#post: returns values in string format for Day
def conToStr(appName = '0invalidName', start = -1.00, end = -1.00):
    #check preconditions
    verNameForm(appName)
    assert (start >= 0 and end >= tStep)
    assert ((start % tStep == 0) and (end % tStep == 0))
    #adjust end time to match proper format
    end = end - tStep 
    #convert times to string format and return complete string
    start = conTimeToStr(start)
    end = conTimeToStr(end)
    return convertedString = appName + start + end

#pre: time is a non-negative multiple of tStep
#post: return time in valid string format
def conTimeToStr(time = -1.00):
    #check preconditions
    assert time >= 0
    assert time % tStep == 0
    #convert time to valid string format
    #divide time by 4 and round to the lowest int and store as hours
    #get remainder of time/4, divide by 0.25, and store as quarter hours

def verStrForm(string = ''):
    "A function to verify format of string used in Day's list of appointments."
    pIs = re.compile('[a-zA-Z]+_[0-2][0-9]h[0-3]q_[0-2][0-9]h[0-3]q')
    pNot = re.compile('[a-zA-Z]+_2[4-9]h[0-3]q_2[4-9]h[0-3]q')
    assert pIs.match(string)
    assert not pNot.match(string)

def verNameForm(name = ''):
    "A function to verify the format of name in a Day compliant string."
    p = re.compile('^[a-zA-Z]+$')
    assert p.match(name)

def verTimeForm(time = ''):
    "A function to verify the format of time in a Day compliant string."
    pIs = re.compile('^_[0-2][0-9]h[0-3]q$')
    pNot = re.compile('^_2[4-9]h[0-3]q$')
    assert pIs.match(time)
    assert not pNot.match(time)


'''
Exceptions
'''

class PreventOverride(Exception):
    "An exception class to prevent previous appointments from being overriden."
    def __init__(self, toAddIn = '', toOverride = ''):
        self.toAddIn = toAddIn
        self.toOverride = toOverride
