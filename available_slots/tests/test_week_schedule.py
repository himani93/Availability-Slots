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
                {datetime.time(06, 00), datetime.time(06, 30)},
                {datetime.time(06, 30), datetime.time(07, 00)},
            ],
            1: [],
            2: [
                {datetime.time(06, 00), datetime.time(06, 30)}
            ],
            3: [
                {datetime.time(9, 00), datetime.time(9, 30)},
                {datetime.time(9, 30), datetime.time(10, 00)},
                {datetime.time(10, 00), datetime.time(10, 30)},
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
            {datetime.time(6, 0), datetime.time(6, 30)}
        ]
