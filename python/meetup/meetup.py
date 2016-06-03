import calendar
from datetime import date


class MeetupDayException(Exception):
    pass


weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
which_rule = {
    '1st': lambda days: days[0],
    '2nd': lambda days: days[1],
    '3rd': lambda days: days[2],
    '4th': lambda days: days[3],
    '5th': lambda days: days[4],
    'last': lambda days: days[-1],
    'teenth': lambda days: [day for day in days if 13 <= day <= 19][0],
}


def meetup_day(year, month, chosen_weekday, which):
    c = calendar.Calendar()
    matching_weekdays = [day for day, weekday in c.itermonthdays2(year, month)
                         if day > 0 and weekday == weekdays.index(chosen_weekday)]
    try:
        day = which_rule[which](matching_weekdays)
    except IndexError:
        raise MeetupDayException()
    return date(year, month, day)