from timerange import TimeRange
from friend import Friend
from custom_list import CustomList


def main():
    available_minutes = CustomList(range(1440))
    f1 = Friend('Jim')
    f1.add_busy_range(TimeRange(start_time='08:00', end_time='10:00'))
    f2 = Friend('Chris')
    f2.add_busy_range(TimeRange(start_time='09:00', end_time='14:00'))
    for m in available_minutes[:]:
        for r in Friend.all_busy_minutes_range:
            if m in r:
                available_minutes.remove_if_exist(m)
    print(available_minutes)

if __name__ == '__main__':
    main()
