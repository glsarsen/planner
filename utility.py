def timerange_to_minutes(t_str):
    """Convert time from string to minutes

    Arguments:
        t_str {str} -- Time in format "hh:mm"
    """
    hour = int(t_str.split(':')[0]) 
    minutes = int(t_str.split(':')[1])
    hour_to_minutes = hour * 60

    return hour_to_minutes + minutes

def minutes_to_timerange_str(m):
    """Return a timerange string in format of HH:MM for the given integer

    Arguments:
        m {int} -- amount of minutes
    """
    hour = m // 60
    minutes = m % 60
    return f"{hour:02d}:{minutes:02d}"

def prettify_available_minutes():
    l = [0, 1, 2, 60, 61, 62]
    # group the list so that: [[0, 1, 2], [60, 61, 62]]
    last = l[0] - 1
    result = []
    part = []
    for elem in l:
        if elem - 1 == last:
            part.append(elem)
        else:
            result.append(part)
            part = [elem]
        last = elem
    result.append(part)
    print(result)

prettify_available_minutes()
