"""
from datetime import date
from unicodedata import lookup

tues = date(2023, 6, 11)

print(tues - date(2023, 6, 10))

print(tues.year)

suits = ['heart', 'diamond', 'spade', 'club']
print([lookup('WHITE ' + s.upper() + ' SUIT') for s in suits])
print([lookup('BLACK ' + s.upper() + ' SUIT') for s in suits])
"""

