Solution to Availability Slots
===============================

Usage:
------

1. `python setup.py install`
2. If slots required from current time use:

   `available-slots --schedule_file <location_of_json_input> --number_of_slots <number_of_slots>`

   If slots required from a specific time use:

   `available-slots --schedule_file <location_of_json_input> --number_of_slots <number_of_slots> --time "YYYY-MM-DD HH:MM"`

Note - Check `available-slots --help` for more info on params.

Example
--------

`available-slots --schedule_file ./available_slots/schedule_3.json --number_of_slots 10 --time "2017-01-01 20:30"`

How to run tests:
-----------------

1. `pip install -r test_requirements.txt`
2. `python setup.py test`

Assumptions:
------------

1. Week starts from Monday
2. Start time is always less than end time.
3. Schedule is always in sorted order
