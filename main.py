import utility as u
from timerange import TimeRange
from friend import Friend
from custom_list import CustomList


def main():
    available_minutes = CustomList(range(1440))
    f1 = Friend('Jim')
    f1.add_busy_range(TimeRange(start_time='08:00', end_time='10:00'))
    f2 = Friend('Chris')
    f2.add_busy_range(TimeRange(start_time='09:00', end_time='14:00'))
    f3 = Friend('Max')
    f3.add_busy_range(TimeRange(start_time='16:15', end_time='21:45'))
    for m in available_minutes[:]:
        for r in Friend.all_busy_minutes_range:
            if m in r:
                available_minutes.remove_if_exist(m)
    for tr in u.prettify_available_minutes(available_minutes):
        print(f"Available time: {tr}")

if __name__ == '__main__':
    main()
