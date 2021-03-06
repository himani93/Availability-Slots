import argparse
import datetime
import json
import pprint
import sys

from available_slots.week_schedule import WeekSchedule
from available_slots.exceptions import *


def read_json_file(file_path):
    with open(file_path) as schedule_file:
        schedule = json.load(schedule_file)

    return schedule

def format_schedule(schedule):
    formatted_schedule = []
    for slot in schedule:
        start_time, end_time = slot
        formatted_schedule.append({
            "start_time": start_time.strftime("%Y-%m-%d %H:%M:%S"),
            "end_time": end_time.strftime("%Y-%m-%d %H:%M:%S")
        })

    return formatted_schedule

def main():
    parser = argparse.ArgumentParser(description="Availability Slots",
                                     add_help=True,
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--schedule_file', dest='schedule_file', required=True,
                        help="Weekly Schedule as per which available schedules is to be found")

    parser.add_argument('--number_of_slots', dest='slots', required=True, type=int,
                        help="Number of available schedule to be retreived")

    parser.add_argument('--time', dest='time', required=False,
                        help="The time from which available slots should be found. Format of time should be YYYY-MM-DD HH:MM")

    if len(sys.argv) < 1:
        parser.print_help()
        sys.exit(1)

    schedule_file =  parser.parse_args().schedule_file
    slots = parser.parse_args().slots

    if parser.parse_args().time:
        try:
            from_time = datetime.datetime.strptime(parser.parse_args().time, "%Y-%m-%d %H:%M")
        except Exception as e:
            raise InvalidDateFormatException("Date: {} should be of format: YYYY-MM-DD HH:mm".format(parser.parse_args().time))
    else:
        from_time = datetime.datetime.now()

    schedule = read_json_file(schedule_file)

    available_schedule = WeekSchedule(schedule).get_n_available_schedule(slots, from_time)
    pprint.pprint(format_schedule(available_schedule))


if __name__ == "__main__":
    main()
