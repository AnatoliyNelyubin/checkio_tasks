from datetime import date
from datetime import timedelta


def checkio(from_date, to_date):
    """
        Count the days of rest
    """
    one_day, current_date, weekends_counter = timedelta(days=1), from_date, 0
    while current_date <= to_date:
        if current_date.weekday() == 5 or current_date.weekday() == 6:
            weekends_counter += 1
        current_date += one_day
    return weekends_counter


if __name__ == '__main__':
    assert checkio(date(2013, 9, 18), date(2013, 9, 23)) == 2, "1st example"
    assert checkio(date(2013, 1, 1), date(2013, 2, 1)) == 8, "2nd example"
    assert checkio(date(2013, 2, 2), date(2013, 2, 3)) == 2, "3rd example"
