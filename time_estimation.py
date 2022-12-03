import datetime

HOURS_A_DAY = 24
HOURS_ASLEEP = 8
WORKING_HOURS = 12
WORKING_BLOCK = 6

TIMING_CHAIN = ['1 min', '10 min', '1 day', '3 days', '7 days', '11 days', '17 days', '21 days']

CARD_MATURE_TO_TIME_MAPPING = {
    '1 min': 40,
     '10 min': 30,
     '1 day': 10,
     '3 days': 20,
     '7 days': 25,
     '11 days': 25,
     '17 days': 25,
     '21 days': 25,
}

# This time mapping indicates the time it takes before pressing the button of the given label.
# For example, after 1 days, we will take 20 seconds to press the '3 days' button

CARDS_TO_MATURITY = len(TIMING_CHAIN)


HEAD_AND_NECK_ANATOMY = 3640

TOTAL_SECONDS_TO_MATURITY = sum(CARD_MATURE_TO_TIME_MAPPING.values())

def calclate_time_required(deck):
    total_time = deck * TOTAL_SECONDS_TO_MATURITY
    hours = total_time / 60 / 60
    print('HOURS:', hours)
    print('WORKING BLOCKS: ', hours / 6)
    print('WORK DAYS: ', hours / 12)
