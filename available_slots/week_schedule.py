import datetime

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
                    start_time, end_time = datetime.time(slot["start_time"]), datetime.time(slot["end_time"])
                    self._schedule[weekday].append({start_time, end_time})
                weekday += 1

    def __repr__(self):
        return "WeekSchedule({})".format(self._schedule)
