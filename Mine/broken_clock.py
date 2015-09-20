def broken_clock(starting_time, wrong_time, error_description):
    import math
    import decimal
    decimal.getcontext().prec =6
    td = {'hours': 3600,
          'minutes': 60,
          'seconds': 1,
          'hour': 3600,
          'minute': 60,
          'second': 1}

    hours, minutes, seconds = starting_time.split(sep=':')
    starting_time_seconds = int(hours) * td['hours'] + float(minutes) * td['minutes'] + float(seconds)
    hours, minutes, seconds = wrong_time.split(sep=':')
    wrong_time_seconds = int(hours) * td['hours'] + float(minutes) * td['minutes'] + float(seconds)
    time_change_value, time_change_measure, dummy_val, interval_value, interval = error_description.split()
    time_change_value = int(time_change_value) * td[time_change_measure]
    interval_value = int(interval_value) * td[interval]
    right_current_time = starting_time_seconds + (wrong_time_seconds - starting_time_seconds)*\
                                                 (interval_value / (interval_value+time_change_value))
    hours = math.floor(right_current_time / td['hours'])
    minutes = math.floor(right_current_time % td['hours'] / td['minutes'])
    seconds = math.floor(right_current_time % td['hours'] % td['minutes'])
    return '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)



#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    assert broken_clock('00:00:00', '00:00:15', '+5 seconds at 10 seconds') == '00:00:10', "First example"
    assert broken_clock('06:10:00', '06:10:15', '-5 seconds at 10 seconds') == '06:10:30', 'Second example'
    assert broken_clock('13:00:00', '14:01:00', '+1 second at 1 minute') == '14:00:00', 'Third example'
    assert broken_clock('01:05:05', '04:05:05', '-1 hour at 2 hours') == '07:05:05', 'Fourth example'
    assert broken_clock('00:00:00', '00:00:30', '+2 seconds at 6 seconds') == '00:00:22', 'Fifth example'
