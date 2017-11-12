'''
Created on 20 April 15
@author:   Ayse Akin
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 11 - Date class
'''
from __builtin__ import True
DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

class Date:
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False
    
    def copy(self):
        ''' Returns a new object with the same month, day, year
        as the calling object (self). '''
        dnew = Date(self.month, self.day, self.year)
        return dnew
    
    def equals(self, d2): 
        '''Decides if self and d2 represent the same calendar date,
            whether or not they are the in the same place in memory.'''
        return self.year == d2.year and self.month == d2.month and \
            self.day == d2.day

    def tomorrow(self):
        '''Returns the date after the calling object.'''
        d = Date(self.month, self.day, self.year)
        if self.isLeapYear() == False:
            if DAYS_IN_MONTH[self.month] == self.day:
                self.day = 1
                self.month += 1
                if self.month == 13:
                    self.month = 1
                    self.year += 1
            else:
                self.day += 1
        else:
            if self.month == 2:
                if DAYS_IN_MONTH[self.month] == self.day-1:
                    self.day = 1
                    self.month += 1
                elif DAYS_IN_MONTH[self.month] == self.day:
                    self.day += 1
                else:
                    self.day += 1
            elif DAYS_IN_MONTH[self.month] == self.day:
                self.day = 1
                self.month += 1
                if self.month == 13:
                    self.month = 1
                    self.year += 1
            else:
                self.day += 1
        d = Date(self.month, self.day, self.year)

    def yesterday(self):
        '''Returns the date before the calling object.'''
        d = Date(self.month, self.day, self.year)
        if self.isLeapYear() == False:
            if self.day == 1:
                if self.month == 1:
                    self.day = 31
                    self.month = 12
                    self.year -= 1
                else:
                    self.day = DAYS_IN_MONTH[self.month -1]
                    self.month -= 1
                    if self.month == 0:
                        self.month = 12
                        self.year -= 1
            else:
                self.day -= 1
        else:
            if self.day == 1:
                if self.month == 3:
                    self.month -= 1
                    self.day = 29
                elif self.month == 1:
                    self.year -= 1
                    self.month = 12
                    self.day = 31
                else:
                    self.day = DAYS_IN_MONTH[self.month -1]
                    self.month -= 1
                    if self.month == 0:
                        self.month = 12
                        self.year -= 1
            else:
                self.day -= 1
        d = Date(self.month, self.day, self.year)
        
    def addNDays(self, N):
        '''Adds a certain number of days to the calling object and returns that date.'''
        d = Date(self.month, self.day, self.year)
        for i in range(N):
            self.tomorrow()
            print self
        d = Date(self.month, self.day, self.year)
    
    def subNDays(self, N):
        '''Subtracts a certain number of days to the calling object and returns that date.'''
        d = Date(self.month, self.day, self.year)
        for i in range(N):
            self.yesterday()
            print self
        d = Date(self.month, self.day, self.year)

    def isBefore(self, d2):
        '''Checks to see if the first date (self.date) is before the second date (d2)'''
        if self.equals(d2):
            return False
        if self.year < d2.year:
            return True
        if self.year == d2.year:
            if self.month < d2.month:
                return True
            if self.month == d2.month:
                if self.day < d2.day:
                    return True
        return False
    
    def isAfter(self, d2):
        '''Checks to see if the first date (self.date) is after the second date (d2)'''
        if self.equals(d2):
            return False
        if self.year > d2.year:
            return True
        if self.year == d2.year:
            if self.month > d2.month:
                return True
            if self.month == d2.month:
                if self.day > d2.day:
                    return True
        return False
    
    def diff(self, d2):
        '''Returns the number of days between the first date (self.date) and the second date (d2)'''
        if self.equals(d2):
            return 0
        date1 = self.copy()
        date2 = d2.copy()
        days = 0
        while date1.equals(date2) == False:
            if date1.isBefore(date2):
                date1.tomorrow()
                days -= 1
            else:
                date2.tomorrow()
                days += 1
        return days
    
    def dow(self):
        '''Returns a string that indicates the day of the week of the object that calls it.'''
        DAYS_OF_WEEK= ['Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday']
        known = 3
        kdate = Date(11, 9, 2011)
        day = self.diff(kdate)
        days = day % 7
        print days
        return DAYS_OF_WEEK[days]