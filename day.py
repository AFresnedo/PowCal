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

# TODO design issue: the client using Day must understand vague string format, oop design would prefer that 
#   using Day with a more general time format would work and that Day would handle its implementation 
#   specific time conversions to store and manipulate
#   note: a possible fix for this is to have a intermediary..but that'll simply be a bandaid to
#   fulfill OOP design at the cost of optimization
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

    #pre: name of appointment(s)
    #post: returns list of strings of appointment(s) in name+start+end format
    def getTime(self, appName = 'noAppointment'):
        #check precondition
        p = re.compile('[a-zA-Z]+')
        assert p.match(appName)
        #get list of appointments with the passed name
        listApp = []
        p = re.compile(appName + '_')
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
    def getName(self, time = '_00h0q'):
        #check precondition
        p = re.compile('_[0-2][0-9]h[0-3]q')
        assert p.match(time) 
        #get string
        index = self.conToInd(time)
        string = self.sch[index]
        #pass string format test and return
        verStrForm(string)
        return string

    #pre: name of appointment
    #post: removes all appointments scheduled with that name
    def delApp(self, appName = 'noAppointment_00h0q_23h3q'):
        #check precondition
        p = re.compile('[a-zA-Z]+')
        assert p.match(appName)
        #replace all matches with noApp string
        p = re.compile(appName + '_')
        for i in range(0, len(self.sch) - 1):
            if p.match(self.sch[i]):
                self.sch[i] = 'noAppointment_00h0q_23h3q'

    #TODO this requires some interpretation of the string
    def clearTime(self, time = '_24h1q'):
        None

    "A method to convert the string version of a start or end time to an index for Day's list."
    def conToInd(self, time = '_12h2q'):
        #compile the regex pattern to search with
        p = re.compile('\d+') #any number
        values = p.findall(time) #get 2 element list [hour, quarter]
        index = 4*int(values[0]) + int(values[1]) #calculate index using hour and quarter
        assert 0<=index<len(self.sch)
        return index

def verStrForm(string = ''):
    "A function to verify format of string used in Day's list of appointments."
    p = re.compile('[a-zA-Z]+_[0-2][0-9]h[0-3]q_[0-2][0-9]h[0-3]q')
    assert p.match(string)

#current implementation of UDT Day in day.py requires interval to be a multiple of 0.25
interval = 0.25 #smallest unit of time is a quarter hour written as 0.25

#pre: appName is a single word, start and end are multiples of interval
#post: returns values in string format for day.Day
def conToStr(day = None, appName = 'noAppointment', start = 0.00, end = 24.00):
    #TODO check preconditions: appName is just a word, start and end are multiples of interval
    assert(day is !None)
    end = end - interval #convert end time to beginning of last interval of time
    fStr = appName + start + end

class PreventOverride(Exception):
    "An exception class to prevent previous appointments from being overriden."
    def __init__(self, toAddIn = '', toOverride = ''):
        self.toAddIn = toAddIn
        self.toOverride = toOverride
