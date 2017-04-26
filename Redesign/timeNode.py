# This object is intended to provide time-based organization for appointments.
# Time nodes are placed in a data structure, most likely a tree, and are most
# useful when targeted in chunks. For example, a user can ask for all
# appointments in a month and then operate on all of them in a chunk or sort
# through the appointments in just a month instead of every appointment. The
# granularity of these nodes are years, months, days, hours, and quarter hours.
# This allows users to ask for a chunk specified by a year, a month, a day, and
# times from 1200 to 1545 for example.

# TODO write gets for every granularity, all return nodes except for quarter
# hours, which return appointments

# write sets for every granularity, all simply need to have appropriate
# dates/times except for quarter hours, which require appointment objects
# make sure you have pre/post...use gets as part of precondition check of nodes
# not already existing

class TimeTargetNode:
    "A node for selecting appointments based on time."
    def __init__(self):
        None
