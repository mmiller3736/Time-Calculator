def add_time(start, duration, weekday='None'):
    colon_loc = start.index(':')
    space_loc = start.index(' ')
    start_arr = [(start[0:colon_loc])]
    start_arr.append((start[colon_loc+1:space_loc]))
    start_arr.append((start[space_loc+1:]))
    duration_arr = duration.split(':')
    new_hours = int(start_arr[0])+int(duration_arr[0])
    new_minutes = int(start_arr[1])+int(duration_arr[1])
    period = start_arr[2]
    hour_change = int(duration_arr[0]) 
    days_later = ''
    weekday_str = ''
    days = 0

    if new_minutes >= 60:
        new_hours = new_hours + int(new_minutes/60)
        hour_change = hour_change + int(new_minutes/60)
        new_minutes = new_minutes % 60
    
    period_change = new_hours//12 % 2
    print(period_change)

    if period == 'AM' and period_change == 0:
        if new_hours >= 24:
            if new_hours >= 48:
                days = new_hours//24
                new_hours = new_hours % 24
                days_later = f'( {days} days later)'
            else:
                days = new_hours//24
                new_hours = new_hours % 24
                days_later = f' (next day)'
        if new_hours > 12:
            new_hours %= 12
            if days > 0:
                days += 1
                days_later = f' ({days} days later)'

    elif period == 'PM' and period_change == 0:
        if new_hours >= 24:
            if new_hours >= 48:
                days = new_hours//24
                new_hours = new_hours % 24
                days_later = f'( {days} days later)'
            else:
                days = new_hours//24
                new_hours = new_hours % 24
                days_later = f' (next day)'
        if new_hours > 12:
            new_hours %= 12
            if days > 0:
                days += 1
                days_later = f' ({days} days later)'

    elif period == 'AM' and period_change == 1:
        period = 'PM'
        if new_hours >= 24:
            if new_hours >= 48:
                days = new_hours//24
                new_hours = new_hours % 24
                days_later = f'( {days} days later)'
            else:
                days = new_hours//24
                new_hours = new_hours % 24
                days_later = f' (next day)'
        if new_hours > 12:
            new_hours %= 12
            if days > 0:
                days += 1
                days_later = f' ({days} days later)'

    elif period == 'PM' and period_change == 1:
        period = 'AM'
        if new_hours >= 24:
            if new_hours >= 48:
                days = new_hours//24
                new_hours = new_hours % 24
                days_later = f'( {days} days later)'
            else:
                days = new_hours//24
                new_hours = new_hours % 24
                days_later = f' (next day)'
        if new_hours > 12:
            new_hours %= 12
            if days > 0:
                days += 1
                days_later = f' ({days} days later)'
            else:
                days_later = f' (next day)'
        elif new_hours == 12:
            if days > 0:
                days += 1
                days_later = f' ({days} days later)'
            else:
                days_later = f' (next day)'

    if new_minutes < 10:
        new_minutes = f'0{new_minutes}'

    if weekday != 'None':
        weekday_arr = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
        cur_weekday = weekday_arr.index(weekday.lower())
        new_weekday_id = (cur_weekday + days) % 7
        new_weekday = weekday_arr[new_weekday_id]
        new_weekday = new_weekday[0].upper() + new_weekday[1:]
        weekday_str = f', {new_weekday}'

    new_time = (f'{new_hours}:{new_minutes} {period}{weekday_str}{days_later}')

    return new_time


print(add_time('2:59 PM', '12:00'))
