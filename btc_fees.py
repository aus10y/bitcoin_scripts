#!/usr/bin/env python3

from urllib.request import urlopen, Request
from pprint import pprint

import json

OUTPUT_TEMPLATE = (
"""
Est Conf Time | Fee (sat/B)
-------------------------------
  Next Block  | {next_blk}+
  1  hr       | {one_hr}+
  4  hr       | {four_hr}+
  12 hr       | {twelve_hr}+
  1 Day       | {one_day}+
  3 Day       | {three_day}+
  7 Day       | {seven_day}+
"""
)


BTC_FEES_ALL_URL = 'https://bitcoinfees.earn.com/api/v1/fees/list'
BTC_FEES_REC_URL = 'https://bitcoinfees.earn.com/api/v1/fees/recommended'

HR = 60
DAY = 1440
_MINUTES = [0, 1 * HR, 4 * HR, 12 * HR, 1 * DAY, 3 * DAY, 7 * DAY]
TIME_RANGES = [(t, _MINUTES[i+1]) for i, t in enumerate(_MINUTES[:-1])]


def build_request(url, headers=None):
    if headers is None:
        headers = {'User-Agent': 'urllib (ubuntu)'}
    return Request(url, headers=headers)


def get_fees():
    r = build_request(BTC_FEES_ALL_URL)
    body = urlopen(r).read()
    return json.loads(body)


def get_fees_recommended():
    r = build_request(BTC_FEES_REC_URL)
    body = urlopen(r).read()
    return json.loads(body)


def calculate_fees(time_groups):
    fees = get_fees()['fees']
    if not fees:
        raise Exception("No Fees!?")
    fees.reverse()

    out = [None for _ in range(len(time_groups) + 1)]

    # Find min fee for next block.
    fee_index = None
    for i, fee in enumerate(fees):
        fee_index = i + 1
        if fee['maxDelay'] == 0:
            out[0] = fee['minFee']
        else:
            break

    # Find min fee for each remaining time group.
    time_index = 0
    for fee in fees[fee_index:]:
        min_time, max_time = time_groups[time_index]

        if min_time < fee['maxMinutes'] <= max_time:
            out[time_index+1] = fee['minFee']
        else:
            if (time_index + 1) < len(time_groups):
                time_index += 1
            else:
                break

    # If we didn't reach each time group, then copy the last min fee to each
    # remaining group.

    final_min = None
    for min_fee in out[::-1]:
        if min_fee is not None:
            final_min = min_fee
            break
    out = [f if f is not None else final_min for f in out]

    return out


if __name__ == '__main__':
    fees = calculate_fees(TIME_RANGES)
    print(OUTPUT_TEMPLATE.format(
        next_blk=fees[0],
        one_hr=fees[1],
        four_hr=fees[2],
        twelve_hr=fees[3],
        one_day=fees[4],
        three_day=fees[5],
        seven_day=fees[6]
    ))
