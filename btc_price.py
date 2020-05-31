#!/usr/bin/env python3

from urllib.request import urlopen, Request

import json


BTC_STATS_URL = 'https://api.pro.coinbase.com/products/BTC-USD/stats'


def build_request(url, headers=None):
    if headers is None:
        headers = {'User-Agent': 'urllib (ubuntu)'}
    return Request(url, headers=headers)


def get_stats():
    r = build_request(BTC_STATS_URL)
    body = urlopen(r).read()
    return json.loads(body)


def format_price(price):
    """Format price with two decimal places."""
    return f"${price:.2f}"


def format_price_bar(stats):
    """Build a string that shows the current price proportionally between the
    days' low and high prices respectively."""

    # Get the prices; format them.
    curr, high, low = map(float, (stats['last'], stats['high'], stats['low']))
    curr_str, high_str, low_str = map(format_price, (curr, high, low))

    # Calculate the current price's position, and how much text should go on
    # either side.
    position = (curr - low) / (high - low)
    separators = (80 - 2) - (len(curr_str) + len(high_str) + len(low_str))
    sep_left = round(separators * position)
    sep_right = separators - sep_left

    return f"{low_str}|{sep_left * '-'}{curr_str}{sep_right * '-'}|{high_str}"

if __name__ == '__main__':
    print(format_price_bar(get_stats()))
