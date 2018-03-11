import argparse
import datetime
import json
import sys

from week_schedule import WeekSchedule


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
    parser = argparse.ArgumentParser(description="Healthify Me Availability Slots",
                                     add_help=True,
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--schedule_file', dest='schedule_file', required=True,
                        help="Weekly Schedule as per which available schedules is to be found")

    parser.add_argument('--number_of_slots', dest='slots', required=True, type=int,
                        help="Number of available schedule to be retreived")

    if len(sys.argv) < 1:
        parser.print_help()
        sys.exit(1)

    schedule_file =  parser.parse_args().schedule_file
    slots = parser.parse_args().slots

    schedule = read_json_file(schedule_file)

    available_schedule = WeekSchedule(schedule).get_n_available_schedule(slots, datetime.datetime.now())
    print format_schedule(available_schedule)


if __name__ == "__main__":
    main()
