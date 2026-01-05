def is_leap_year(year):
    if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
        return True
    else:
        return False


is_leap_year(2400)
is_leap_year(1989)