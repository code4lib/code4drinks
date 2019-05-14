#!/usr/bin/env python

# cat ~/irclogs/freenode/#code4lib.log | ./stats.py

import re
import csv
import sys

from collections import Counter

nicks = Counter()
drinks = Counter()

for line in sys.stdin:
    m = re.search(r'zoia (fills a pint glass with|brews and pours a pot of|brews and pours a cup of) (.+), and sends it sliding down the bar to (\w+)( \()?', line)
    if m:
        nicks[m.group(3)] += 1
        drinks[m.group(2)] += 1

def write_csv(filename, counter, headings):
    with open(filename, 'w') as fh:
        out = csv.writer(fh)
        out.writerow(headings)
        for label, count in counter.most_common():
            out.writerow([label, count])

write_csv("nicks.csv", nicks, ['nick', 'drinks'])
write_csv("drinks.csv", drinks, ['drink', 'count'])
