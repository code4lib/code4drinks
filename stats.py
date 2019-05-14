#!/usr/bin/env python

# cat ~/irclogs/freenode/#code4lib.log | ./stats.py

import re
import csv
import sys

from collections import Counter

nicks = Counter()
coffees = Counter()

for line in sys.stdin:
    m = re.search(r'zoia brews and pours a cup of (.+), and sends it sliding down the bar to (\w+) \(?', line)
    if m:
        nicks[m.group(1)] += 1
        coffees[m.group(2)] += 1
        
with open('nicks.csv', 'w') as fh:
    out = csv.writer(fh)
    out.writerow(['nick', 'coffees'])
    for nick, coffee in nicks.items():
        out.writerow([nick, coffee])

with open('coffees.csv', 'w') as fh:
    out = csv.writer(fh)
    out.writerow(['coffee', 'served'])
    for coffee, served in coffees.items():
        out.writerow([coffee, served])





