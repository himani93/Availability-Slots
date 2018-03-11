import datetime
import pytest

from available_slots.week_schedule import WeekSchedule


class TestWeekSchedule(object):

    def test_empty_week_schedule(self):
        expected_party_schedule = {weekday: [] for weekday in range(7)}

        assert WeekSchedule(None)._schedule == expected_party_schedule
        assert WeekSchedule([])._schedule == expected_party_schedule
        assert WeekSchedule([ [],[],[],[],[],[],[] ])._schedule == expected_party_schedule

    def test_week_schedule(self):
        schedule = [
            [  # Monday
                {"start_time": "06:00", "end_time": "06:30"},
                {"start_time": "06:30", "end_time": "07:00"},
            ], [  # Tuesday
            ], [  # Wednesday
                {"start_time": "06:00", "end_time": "06:30"},
            ], [  # Thursday
                {"start_time": "09:00", "end_time": "09:30"},
                {"start_time": "09:30", "end_time": "10:00"},
                {"start_time": "10:00", "end_time": "10:30"},
            ], [  # Friday
            ], [  # Saturday
            ], [  # Sunday
            ]
        ]
        expected_schedule = {
            0: [  # Monday
                (datetime.time(06, 00), datetime.time(06, 30)),
                (datetime.time(06, 30), datetime.time(07, 00)),
            ],
            1: [],
            2: [
                (datetime.time(06, 00), datetime.time(06, 30))
            ],
            3: [
                (datetime.time(9, 00), datetime.time(9, 30)),
                (datetime.time(9, 30), datetime.time(10, 00)),
                (datetime.time(10, 00), datetime.time(10, 30)),
            ],
            4: [],
            5: [],
            6: [],
        }

        assert WeekSchedule(schedule)._schedule == expected_schedule

    def test_weekday_schedule(self):
        assert WeekSchedule([]).get_weekday_schedule(0) == []

        schedule = [
            [  # Monday
                {"start_time": "06:00", "end_time": "06:30"},
                {"start_time": "06:30", "end_time": "07:00"},
            ], [  # Tuesday
            ], [  # Wednesday
                {"start_time": "06:00", "end_time": "06:30"},
            ], [  # Thursday
                {"start_time": "09:00", "end_time": "09:30"},
                {"start_time": "09:30", "end_time": "10:00"},
                {"start_time": "10:00", "end_time": "10:30"},
            ], [  # Friday
            ], [  # Saturday
            ], [  # Sunday
            ]
        ]
        party_schedule = WeekSchedule(schedule)
        assert party_schedule.get_weekday_schedule(1) == []
        assert party_schedule.get_weekday_schedule(2) == [
            (datetime.time(6, 0), datetime.time(6, 30))
        ]

    def test_available_day_schedule(self):
        current_time = datetime.datetime(2018, 03, 10, 0, 0)
        schedule = [
            [  # Monday
                {"start_time": "06:00", "end_time": "06:30"},
                {"start_time": "06:30", "end_time": "07:00"},
            ], [  # Tuesday
            ], [  # Wednesday
                {"start_time": "06:00", "end_time": "06:30"},
            ], [  # Thursday
                {"start_time": "09:00", "end_time": "09:30"},
                {"start_time": "09:30", "end_time": "10:00"},
                {"start_time": "10:00", "end_time": "10:30"},
            ], [  # Friday
            ], [  # Saturday
            ], [  # Sunday
            ]
        ]
        party_schedule = WeekSchedule(schedule)  # Saturday
        available_schedule = party_schedule.get_available_day_schedule(current_time)
        assert available_schedule == []

        current_time = datetime.datetime(2018, 03, 7, 0, 0)  # Wednesday
        available_schedule = party_schedule.get_available_day_schedule(current_time)
        assert available_schedule == [(datetime.datetime(2018, 03, 7, 06, 00), datetime.datetime(2018, 03, 7, 06, 30))]

        current_time = datetime.datetime(2018, 03, 7, 12, 00)  # Wednesday
        available_schedule = party_schedule.get_available_day_schedule(current_time)
        assert available_schedule == []

        current_time = datetime.datetime(2018, 03, 8, 9, 45)  # Thursday
        available_schedule = party_schedule.get_available_day_schedule(current_time)
        assert available_schedule == [
            (datetime.datetime.combine(current_time.date(), datetime.time(10, 00)), datetime.datetime.combine(current_time.date(), datetime.time(10, 30))),
        ]

    def test_n_available_schedule(self):
        current_time = datetime.datetime(2018, 03, 10, 0, 0)
        schedule = [
            [  # Monday
                {"start_time": "06:00", "end_time": "06:30"},
                {"start_time": "06:30", "end_time": "07:00"},
            ], [  # Tuesday
            ], [  # Wednesday
                {"start_time": "06:00", "end_time": "06:30"},
            ], [  # Thursday
                {"start_time": "09:00", "end_time": "09:30"},
                {"start_time": "09:30", "end_time": "10:00"},
                {"start_time": "10:00", "end_time": "10:30"},
            ], [  # Friday
            ], [  # Saturday
            ], [  # Sunday
            ]
        ]
        party_schedule = WeekSchedule(schedule)  # Saturday
        available_schedule = party_schedule.get_n_available_schedule(1, current_time)
        assert available_schedule == [(datetime.datetime(2018, 03, 12, 6, 0), datetime.datetime(2018, 3, 12, 6, 30))]

        available_schedule = party_schedule.get_n_available_schedule(3, current_time)
        assert available_schedule == [(datetime.datetime(2018, 03, 12, 6, 0), datetime.datetime(2018, 3, 12, 6, 30)),
                                      (datetime.datetime(2018, 03, 12, 6, 30), datetime.datetime(2018, 3, 12, 7, 0)),
                                      (datetime.datetime(2018, 03, 14, 6, 0), datetime.datetime(2018, 3, 14, 6, 30))]

        current_time = datetime.datetime(2018, 03, 8, 9, 45)
        available_schedule = party_schedule.get_n_available_schedule(1, current_time)
        assert available_schedule == [(datetime.datetime(2018, 03, 8, 10, 0), datetime.datetime(2018, 3, 8, 10, 30))]

        current_time = datetime.datetime(2018, 03, 8, 9, 0)
        available_schedule = party_schedule.get_n_available_schedule(1, current_time)
        assert available_schedule == [(datetime.datetime(2018, 03, 8, 9, 0), datetime.datetime(2018, 3, 8, 9, 30))]

    def test_get_schedule_when_empty(self):
        schedule = [
            [  # Monday
            ], [  # Tuesday
            ], [  # Wednesday
            ], [  # Thursday
            ], [  # Friday
            ], [  # Saturday
            ], [  # Sunday
            ]
        ]
        current_time = datetime.datetime(2018, 3, 11, 3, 9)
        party_schedule = WeekSchedule(schedule)  # Saturday
        available_schedule = party_schedule.get_n_available_schedule(1, current_time)
        assert available_schedule == []
