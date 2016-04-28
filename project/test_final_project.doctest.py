'''
>>> def is_leap_year(1996):
     if (year % 4 == 0):
         print("is a Leap Year.", 1996);

    return True

    else:
     if (year % 100 == 0):
         print("is not a Leap Year.", 1990);

    return False

    else:
         if (year % 400 == 0):
             print("is a Leap Year.", 1996);

    return True
'''






if __name__ == "__main__":
    import doctest
    doctest.testmod()