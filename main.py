import json
from scraper.gcal_parser import fetch_gcal_events

def main():
    events = fetch_gcal_events()

    with open("data/tickets.json", "w", encoding="utf-8") as f:
        json.dump(events, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
