
def is_leap_year(year):
    ''' Returns True for leap years, False for others

    >>> is_leap_year(1996)
    True
    >>> is_leap_year(1990)
    False
    '''
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

