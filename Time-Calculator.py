def add_time(start: str, duration: str, week: str = '') -> str:
   
    # Days of the week
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    # Split into hours, minutes and pm or am
    start_time, am_pm = start.split()
    start_hours, start_minutes = map(int, start_time.split(':'))

    # Convert start time to 24-hour format
    if am_pm == 'PM' and start_hours != 12:
        start_hours += 12
    elif am_pm == 'AM' and start_hours == 12:
        start_hours = 0
    
    # Split into hours and minutes
    duration_hours, duration_minutes = map(int, duration.split(':'))
    
    # calculate total hours and minutes
    total_minutes = start_minutes + duration_minutes
    total_hours = start_hours + duration_hours + (total_minutes // 60)
    total_minutes %= 60
    
    # calculate the number of days later
    days_later = total_hours // 24
    total_hours %= 24
    
    # Convert back to 12-hour format
    am_pm = 'AM' if total_hours < 12 else 'PM'
    total_hours = total_hours if total_hours != 0 else 12
    total_hours = total_hours if total_hours <= 12 else total_hours - 12
    
    # Determine the new day of the week if provided
    actual_day = ''
    if week:
        week = week.capitalize()
        if week in days:
            start_day_index = days.index(week)
            actual_day = days[(start_day_index + days_later) % 7]
    
    # Format days later message
    if days_later == 1:
        day_suffix = ' (next day)'
    elif days_later > 1:
        day_suffix = f' ({days_later} days later)'
    else:
        day_suffix = ''
    
    # final output
    new_time = f"{total_hours}:{total_minutes:02d} {am_pm}"
    if actual_day:
        new_time += f", {actual_day}"
    new_time += day_suffix
    
    print(new_time)
    return new_time

add_time('10:10 PM', '3:30')
