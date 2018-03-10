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
                    self._schedule[weekday].append((start_time, end_time))
                weekday += 1

    def __repr__(self):
        return "WeekSchedule({})".format(self._schedule)

    def get_weekday_schedule(self, weekday):
        if not (0 <= weekday <= 6):
            return InvalidWeekdayException("Invalid weekday passed: {}".format(weekday))
        return self._schedule[weekday]

    def get_available_day_schedule(self, day):
        weekday_schedule = self.get_weekday_schedule(day.weekday())

        time = day.time()
        available_schedule = []
        for schedule in weekday_schedule:
            start_time, end_time = schedule
            if start_time >= time:
                available_day_slot = (datetime.combine(day.date(), start_time), datetime.combine(day.date(), end_time))
                available_schedule.append(available_day_slot)

        return available_schedule
