from datetime import datetime

from collections import defaultdict


class WeekSchedule(object):
    def __init__(self, schedule):
        WEEKDAYS = 7
        self._schedule = defaultdict(list)

        for weekday in range(WEEKDAYS):
            self._schedule[weekday] = []

        if schedule:
            weekday = 0
            for day_schedule in schedule[:WEEKDAYS]:
                for slot in day_schedule:
                    start_time, end_time = datetime.strptime(slot["start_time"], "%H:%M").time(), datetime.strptime(slot["end_time"], "%H:%M").time()
                    self._schedule[weekday].append({start_time, end_time})
                weekday += 1

    def __repr__(self):
        return "WeekSchedule({})".format(self._schedule)
