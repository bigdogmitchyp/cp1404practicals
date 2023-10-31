"""
CP1404 prac module
est time = 10 min
start time = 1326
end time = 1334
total time = 8 min
"""

from prac_06.guitar import Guitar

gibson_l5_ces = Guitar("Gibson L-5 CES", 1922, 16035.40)
don_big_strum = Guitar("DONSBIGSTRUM", 2013, 1000000000)
print(f"expecting 101 got {gibson_l5_ces.get_age()}")
print(f"expecting 10 got {don_big_strum.get_age()}")
print(f"expecting True got {gibson_l5_ces.is_vintage()}")
print(f"expecting False got {don_big_strum.is_vintage()}")
