import datetime


def get_today_date():
    current_date = datetime.datetime.now().date()
    # Format the date as "Month Day, Year"
    formatted_date = current_date.strftime("%b %-d, %Y")
    return current_date, formatted_date
