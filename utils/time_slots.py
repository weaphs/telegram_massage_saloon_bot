from datetime import datetime,date, time, timedelta

def generate_free_slots( search_date: date ,
    start: time = time(9, 0),
    end: time = time(18, 0),
    interval_hours: int = 1) -> list[str]:

    slots = []
    current = datetime.combine(search_date, start)
    end_dt = datetime.combine(search_date, end)

    while current <= end_dt:
        slots.append(current.strftime("%H:%M"))
        current += timedelta(hours=interval_hours)

    return slots

