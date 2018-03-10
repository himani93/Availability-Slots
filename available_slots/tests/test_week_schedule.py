import datetime
import pytest

from available_slots.week_schedule import WeekSchedule


class TestWeekSchedule(object):

    def test_week_schedule(self):
        expected_party_schedule = {weekday: [] for weekday in range(7)}

        assert WeekSchedule(None)._schedule == expected_party_schedule
        assert WeekSchedule([])._schedule == expected_party_schedule
