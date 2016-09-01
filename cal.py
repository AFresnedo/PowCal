"""
This module is intended to manage a calendar using Day UDTs. The calendar is designed to provide
enough information to the client to answer most questions a human could ask and answer of a calendar
full of appointments.

Created by AFresnedo for use with the Day module and Pow module in the PowCal project.
"""

import day
import dataStruc

#TODO check singleton and python
class Cal:
    "A singleton calendar storing appointments and their info for a client to view and manipulate."
    def __init__(self):
        appMap = AppMap()
        appTree = AppTree()

    #this method updates a pre-existing appointment's info
    def updateInfo(self, time = -1.00):
        None #add information to an appointment to allow for double+ booking or fixing
        #problem with above idea is that the name can't change because the keys are already made
        #   basically the implmentation of this is deleting and adding newly updated files with some
        #   shortcuts possible

#TODO make sure adding an appointment adds it to both the tree and the map, likewise deleting.
#   this is important so that using the date & hours as a key will always result in unique keys

#TODO some kind of management for hours in a day...resizing appointments?

#TODO count how many days in a month have appoints (and similiar)

#TODO count how many appointments in a day (different from above)

#TODO how many hours of video games played? what does this even look like? get all appointments
#   in a certain timespan and then parse their infos? i guess, would need some sort of "type"
#   standard in all appointment info files
#   rememember cal only needs to provide the ability to do this, pow is the one who figures out
#   what is a video game etc...as long as cal can grab what is needed and has stored the data

#TODO how much free time left in day X?

#TODO add appointment with time <> and info <>
#TODO delete appointment
#TODO update appointment...just the info? how about changing the name in the tree too?
