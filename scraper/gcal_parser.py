import requests
import icalendar
from datetime import datetime, timedelta

ICS_URL = "https://calendar.google.com/calendar/ical/lilribbon.sche@gmail.com/public/basic.ics"

def fetch_gcal_events():
    resp = requests.get(ICS_URL, timeout=10)
    resp.raise_for_status()

    cal = icalendar.Calendar.from_ical(resp.text)
    events = []

    now = datetime.now()
    one_month_later = now + timedelta(days=30)

    for component in cal.walk():
        if component.name != "VEVENT":
            continue

        title = str(component.get("summary"))
        start = component.get("dtstart").dt
        end = component.get("dtend").dt
        desc = component.get("description")
        loc = component.get("location")

        # dtstart が date の場合に対応
        if isinstance(start, datetime):
            event_start = start
        else:
            event_start = datetime.combine(start, datetime.min.time())

        if not (now <= event_start <= one_month_later):
            continue

        # dtend が date の場合に対応
        if isinstance(end, datetime):
            event_end = end
        else:
            event_end = datetime.combine(end, datetime.min.time())

        events.append({
            "title": title,
            "start": event_start.strftime("%Y-%m-%d %H:%M"),
            "end": event_end.strftime("%Y-%m-%d %H:%M"),
            "description": desc or "",
            "location": loc or "",
            "source": ICS_URL
        })

    events.sort(key=lambda x: x["start"])
    return events
