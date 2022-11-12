from datetime import datetime


def time_interval(dt1, dt2=datetime.now()):
    difer = abs(dt2 - dt1)
    difer_years = int(difer.days//365.2425)
    difer_months = int((difer.days-(difer_years*365.2425))//30.437)
    difer_days = int(difer.days-(difer_years*365.2425)-(difer_months*30.437))
    return f"{difer_years} years and {difer_months} months and {difer_days} days"


print('We have', time_interval(datetime(2010, 5, 13, 12, 00)), 'of relationship')
print('We have', time_interval(datetime(2016, 5, 12, 12, 00)), 'of marriage')
